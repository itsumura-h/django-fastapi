FROM nginx:alpine

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8

# ツールをインストール
RUN apk --update --no-cache add openssl
RUN apk add vim

# ルートディレクトリを作成
RUN mkdir -p /var/www/html
# ソケット用ディレクトリを作成
RUN mkdir -p /var/run/sock

# # 設定ファイル
# ADD nginx.conf /etc/nginx/nginx.conf
# ADD default.conf /etc/nginx/sites-available/default
# ADD default.conf /etc/nginx/sites-enabled/default
# ADD start-nginx.sh /