# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app
COPY . .

RUN apt-get update \
    && apt-get -y install libpq-dev gcc
RUN pip install -r requirements.txt

ENV FLASK_APP=app.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]