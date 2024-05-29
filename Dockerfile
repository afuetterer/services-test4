FROM python:3.12-slim

ARG VERSION

WORKDIR /app

COPY pyproject.toml .
COPY README.md .
COPY src ./src

RUN python -m pip install .
