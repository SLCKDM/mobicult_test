du:
	docker compose up -d
dub:
	docker compose up --build -d
dd:
	docker compose down
wu:
	celery -A worker.app:app worker --loglevel=INFO