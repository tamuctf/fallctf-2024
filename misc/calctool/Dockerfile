from python:3.11-slim as base

RUN pip install --no-cache-dir Flask sympy

RUN mkdir /app
WORKDIR /app

COPY templates/ ./templates
COPY ./server.py .
COPY ./flag.txt .

ENTRYPOINT ["python3", "server.py"]