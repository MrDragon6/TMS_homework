*Тут будет описание проекта*

Локальный запуск проекта
========================

1. Создать .env файл для dev окружения: `сp config/.env.dist config/.env`
2. Указать подключение к БД в `config/.env` `BUSDOCS_SQLALCHEMY_DATABASE_URI`
3. Установить расширения в БД : `CREATE EXTENSION pgcrypto; CREATE EXTENSION pg_trgm;`
4. Запустить миграции: `python main.py db upgrade`

Запуск
======

Запуск сервера для разработки: 
- `python main.py runserver` - flask-приложение
- `python main.py run_mq` - mq воркер

По-умолчанию сервер слушет адрес `0.0.0.0:2000`.
Чтобы указать другой: `python main.py runserver {host} {port}`

Запуск dev окружения в docker
=============================

Сборка `docker-compose -f docker-compose.dev.yml build app db`

Миграции `docker-compose -f docker-compose.dev.yml run app python3.7 main.py db upgrade`

Запуск `docker-compose -f docker-compose.dev.yml up`



Миграции
========

Применить миграции: `python main.py db upgrade`

Откатить миграции: `python main.py db downgrade`

Сгенерировать миграцию: `python main.py db migrate --rev-id 0000 --message model_changes_description`

Тесты
=====

Тесты запускаются командой `pytest`.

Для нормальной работы тестов у пользователя БД должна быть роль `SUPERUSER`.
Это связано с тем, что каждый раз при выполнении тестов создается отдельная БД и в неё устанавливаются расширения.

Запуск тестов в docker-контейнере `docker-compose -f docker-compose.tests.yml run --rm tests`
Очистка окружения после тестов `docker-compose -f docker-compose.tests.yml down`
