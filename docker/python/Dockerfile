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
# poetryが作る仮想環境をプロジェクトディレクトリ内にする
RUN poetry config virtualenvs.in-project true
# ログディレクトリを作る
WORKDIR /var/log/fastapi
WORKDIR /var/log/django
# 起動場所
WORKDIR /home
