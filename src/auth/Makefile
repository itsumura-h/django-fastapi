.PHONY: dev
dev:
	poetry run python manage.py runserver 0.0.0.0:8001

.PHONY: serve
serve:
	poetry run gunicorn config.wsgi -c gunicorn.py --reload
