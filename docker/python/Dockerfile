FROM python:3-slim
RUN apt update && \
    apt upgrade -y && \
    apt install -y \
        gcc \
        g++ \
        libffi-dev \
        libc-dev \
        git \
        make \
        graphviz \
        sqlite3

RUN pip install poetry pylint
# poetry install
WORKDIR /home
ADD ./src/poetry.lock /home
ADD ./src/pyproject.toml /home
RUN poetry install
# ログディレクトリを作る
WORKDIR /var/log/fastapi
WORKDIR /var/log/django
# 起動場所
WORKDIR /home
