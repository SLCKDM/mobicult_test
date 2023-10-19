FROM python:3.11-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app/
COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn main:app --host loclhost --port 8000