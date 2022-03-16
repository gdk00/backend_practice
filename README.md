# Практика бекенда

## Разработка

Установка менеджера пакетов [Poetry](https://python-poetry.org)

```sh
# Для Linux/Mac/WSL
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
# Для Windows Power Shell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

Установка зависимостей

```sh
poetry install
```

Запуск проекта

```sh
poetry run python ./src/run.py
```

Автоматическая сортиовка импортов в файлах (косметика)

```sh
poetry run isort .
```

---

## Postman

Для отладки приложения можно использовать тулзу `Postman` ([скачать](https://www.postman.com/downloads/)).
После этого в программе можно импортировать готовую коллекцию запросов из этого репозитория: `BackendPractice.postman_collection.json`.

---

## Задание

После успешной установки и запуска проекта похлопайте себя по плечу.
Далее давайте сделаем ...

---

## Ресурсы

1. [FastApi](https://fastapi.tiangolo.com)
1. [SQLAlchemy](https://docs.sqlalchemy.org)
1. [Poetry](https://python-poetry.org)
1. [Postman](https://learning.postman.com)
1. [Pydantic](https://pydantic-docs.helpmanual.io)
1. [Swagger](https://swagger.io)
