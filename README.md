# Практика бекенда

## Разработка

Установка менеджера пакетов

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
