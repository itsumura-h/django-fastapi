Django FastAPI
===

# コンテナを起動
## 開発環境
```
docker-compose build
docker-compose up -d
docker-compose exec app sh

# FastAPIのプロジェクトの環境構築
cd /home/app
source .venv/bin/activate
poetry env use .venv/bin/python
poetry install

# venvから抜ける
deactivate

# Djangoのプロジェクトの環境構築
cd /home/auth
source .venv/bin/activate
poetry env use .venv/bin/python
poetry install
python manage.py migrate

# venvから抜ける
deactivate

# 管理画面を起動
cd /home/auth
make dev

# アプリケーションを起動
cd /home/app
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
コンテナ内で`/app/src`ディレクトリを開く。

```bash
poetry install
```
を実行する。

プロジェクトディレクトリ内に`.venv`という仮想環境のディレクトリが作られるので、  
VSCodeの下にある「Select python interpreter」をクリックし、「Enter interpreter path」を選択し、`/app/src/.venv/bin/python3`を選ぶ。
