.PHONY: dev
dev:
	poetry run uvicorn main:app --host 0.0.0.0 --reload

.PHONY: serve
serve:
	poetry run gunicorn main:app -c gunicorn.py --reload

.PHONY: mypy
mypy:
	poetry run mypy ./main.py

.PHONY: class
class:
	poetry run pyreverse -o png -p Project -AS /app/src
	mv /app/src/classes_Project.png /app/documents/クラス図/
	mv /app/src/packages_Project.png /app/documents/クラス図/
