FROM python:3.11-slim

WORKDIR /api
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install poetry
COPY pyproject.toml pyproject.toml
RUN poetry install

COPY . .