# Техническое задание: DBService для VPN‑бота

## 1. Общие требования

- Язык: **Python 3.12+**
- Веб‑фреймворк: **FastAPI**
- База данных: **PostgreSQL 14+**
- ORM: **SQLAlchemy 2.x** (declarative, sync или async — на выбор при реализации)
- Миграции: **Alembic**
- Схемы/валидация: **Pydantic v2**
- Спецификация API: **OpenAPI 3.0.3** (`DBService/openapi.yaml` — источник правды)
- Генерация кода: **OpenAPI Generator** (серверные модели и базовые эндпоинты)
- Развёртывание: **Docker** (один контейнер с приложением и миграциями при старте)
- Сервис работает только с БД (без сложного бизнес‑service‑слоя поверх репозиториев).

## 2. Архитектура и структура проекта

Корневая структура для `DBService` (слоистая, без отдельного service layer, с использованием `internal/`):

```text
DBService/
├── app/
│   ├── __init__.py
│   └── main.py              # Точка входа FastAPI (импортирует всё из internal)
│
├── internal/
│   ├── api/                 # Роуты (endpoints), сгруппированные по ресурсам
│   │   ├── __init__.py
│   │   ├── deps.py          # Общие зависимости (сессия БД и т.п.)
│   │   ├── health.py        # /health
│   │   ├── configs.py       # /configs
│   │   ├── users.py         # /users, /users/{id}, /users/{id}/carma
│   │   ├── carma.py         # /carma-events
│   │   ├── servers.py       # /servers
│   │   ├── subscriptions.py # /subscriptions
│   │   └── applications.py  # /applications
│   ├── models/              # SQLAlchemy ORM‑модели (таблицы Postgres)
│   │   ├── __init__.py
│   │   ├── base.py          # Base = declarative_base(), metadata
│   │   ├── configs.py
│   │   ├── servers.py
│   │   ├── users.py
│   │   ├── carma.py
│   │   ├── carma_events.py
│   │   ├── applications.py
│   │   └── subscriptions.py
│   ├── schemas/             # Pydantic‑схемы (DTO) для запросов/ответов
│   │   ├── __init__.py
│   │   ├── configs.py
│   │   ├── users.py
│   │   ├── carma.py
│   │   ├── servers.py
│   │   ├── applications.py
│   │   └── subscriptions.py
│   └── repositories/        # Доступ к БД (CRUD, выборки) поверх ORM
│       ├── __init__.py
│       ├── configs.py
│       ├── users.py
│       ├── carma.py
│       ├── servers.py
│       ├── applications.py
│       └── subscriptions.py
│
├── utils/                   # Общая инфраструктура и утилиты (вне internal)
│   ├── __init__.py
│   ├── config.py            # Чтение env (DATABASE_URL и др.)
│   ├── db.py                # Создание engine, SessionLocal и зависимостей FastAPI
│   ├── logging.py           # Базовая настройка логирования
│   └── time.py              # Вспомогательные функции, если понадобятся
│
├── openapi.yaml             # Текущая спецификация API (уже есть)
├── TECH_SPEC.md             # Данный файл ТЗ
├── requirements.txt         # Зависимости Python
├── alembic.ini              # Конфиг Alembic
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/            # Миграции (initial + последующие)
│       └── xxxx_initial.py
├── Dockerfile               # Образ для запуска приложения
└── docker-compose.yml       # (опционально) Postgres + DBService в одной сети
```

### 2.1. `app/main.py`

- Точка входа FastAPI.
- Создаёт объект `FastAPI`.
- Импортирует и подключает роутеры из `internal.api.*` с тегами из OpenAPI.
- Настраивает lifespan (подключение/отключение БД — при необходимости) через функции из `utils.db`.

### 2.2. Роуты (`internal/api/*.py`)

- Каждый файл соответствует группе тегов/ресурсов:
  - `configs.py` — все эндпоинты `/configs` и `/configs/{id}`.
  - `users.py` — `/users`, `/users/{user_id}`, `/users/count`.
  - `carma.py` — `/users/{user_id}/carma`, `/carma-events`, `/carma-events/{id}`.
  - `servers.py` — `/servers`, `/servers/{id}`, `/servers/best`, `/servers/{id}/start/stop`.
  - `subscriptions.py` — `/subscriptions`, `/subscriptions/{id}`, `/subscriptions/{id}/extend`, `/subscriptions/revoke-expired`.
  - `applications.py` — `/applications`, `/applications/{id}`, `/applications/{id}/approve`.
- Роуты обращаются **напрямую к репозиториям** (`internal.repositories.*`) и возвращают Pydantic‑схемы из `internal.schemas`.

### 2.3. Модели (`internal/models`)

- Для каждой сущности из `API.md` / `openapi.yaml` — отдельная ORM‑модель:
  - `Config`, `Server`, `User`, `Carma`, `CarmaEvent`, `Application`, `Subscription`.
- Модели определяют:
  - названия таблиц;
  - типы полей (включая enum‑ы и nullable‑флаги);
  - связи `relationship` (например, `Subscription` ↔ `Config`).

### 2.4. Схемы (`internal/schemas`)

- Pydantic‑модели для запросов и ответов, максимально близко к OpenAPI:
  - `Config`, `ConfigCreate`, `ConfigUpdate` и т.п.
- Используются в сигнатурах эндпоинтов (`response_model`, `Body`).

### 2.5. Репозитории (`internal/repositories`)

- Инкапсулируют все запросы к БД:
  - методы `get_by_id`, `list`, `create`, `update`, `delete`.
  - специфичные операции (поиск лучшего сервера, `revoke_expired` и т.п.).
- Работают с SQLAlchemy сессией, полученной через зависимость FastAPI из `internal.api.deps` / `utils.db`.

### 2.6. Утилиты и инфраструктура (`utils`)

- `config.py`:
  - Pydantic Settings или простой класс для чтения переменных окружения:
    - `DATABASE_URL`
    - `APP_ENV`
    - опционально: порт, debug‑флаги.
- `db.py`:
  - создание `engine`;
  - `SessionLocal` (или async sessionmaker);
  - зависимость `get_db()` для FastAPI, возвращающая сессию с контекстным менеджером.
- `logging.py`:
  - базовая настройка логирования (формат, уровень).
- `time.py`:
  - вспомогательные функции, если понадобятся.

---

## 3. Работа с БД и миграциями

### 3.1. Подключение к PostgreSQL

- Используется строка подключения `DATABASE_URL` из окружения.
- Поддерживаются как sync, так и async драйверы (решается при реализации).
- Обязательно: пул подключений (по умолчанию параметры драйвера, настройки можно расширить позже).

### 3.2. Миграции Alembic

- `alembic/env.py` должен использовать метадату из `app.models.base`.
- Первая миграция `xxxx_initial.py` создаёт все таблицы:
  - `configs`, `servers`, `users`, `carma`, `carma_events`, `applications`, `subscriptions`.
- При старте контейнера выполняется `alembic upgrade head`.

---

## 4. API‑контракт

- Реализовать все эндпоинты, описанные в `DBService/openapi.yaml`:
  - сигнатуры (методы, пути, query‑параметры, body);
  - структуры ответов (Pydantic‑схемы);
  - статусы ответов (200/201/204 и т.д.).
- Все операции чтения списков должны поддерживать `limit` и `offset` в соответствии со схемой.
- Операции, описанные как "атомарные" (например, одобрение заявки → создание/продление подписки → изменение кармы → создание события), должны выполняться в рамках одной транзакции БД.

---

## 5. Конфигурация и развёртывание (Docker)

### 5.1. Dockerfile

- Базовый образ Python 3.12.
- Шаги:
  1. Копировать `requirements.txt` и установить зависимости.
  2. Копировать исходники `DBService/`.
  3. Запуск entrypoint‑скрипта, который:
     - выполняет `alembic upgrade head`;
     - запускает uvicorn с `app.main:app`.

### 5.2. docker‑compose (опционально)

- Сервисы:
  - `db` — Postgres с инициализацией БД;
  - `dbservice` — текущий сервис, зависящий от `db`.
- Оба сервиса в одной внутренней сети, без внешней экспозиции DBService, если он нужен только боту/другим контейнерам.

---

Этот файл описывает целевую структуру и требования к реализации DBService. Детали моделей и эндпоинтов берутся из `API.md` и `openapi.yaml` и считаются обязательными для соблюдения при разработке.
