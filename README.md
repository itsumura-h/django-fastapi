Django FastAPI
===

# コンテナを起動
## 開発環境
```
docker-compose build
docker-compose up -d
docker-compose exec app sh

# アプリケーションを起動
cd /home/app
make dev

# 管理画面を起動
cd /home/auth
poetry run python manage.py migrate
make dev
```

## 本番環境
```
docker-compose -f docker-compose.prod.yaml up -d
```

# 開発環境構築手順

## IDE
VSCodeに`Remote Container`の拡張機能を入れる。  
VSCode左下の「><」をクリックして、コンテナに接続する。

## 補完が効くようにする。

VSCodeに`Python`の拡張機能を入れる。  
VSCodeの下にある「Select python interpreter」をクリックし、「Enter interpreter path」を選択し、`/root/.cache/pypoetry/virtualenvs/home-********-py3.8/bin/python3`を選ぶ。  
※　`********` は乱数