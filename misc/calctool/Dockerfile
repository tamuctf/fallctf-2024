from python:3.11-slim as base

RUN pip install --no-cache-dir flask sympy

RUN mkdir /app
WORKDIR /app

COPY ./server.py .
COPY ./flag.txt .

CMD ["python3", "server.py"]