# Dockerfile

# Copyright 2024 Qi Tianshi. All rights reserved.


# Sets up the environment.
FROM python:3.10-slim
ENV PORT=8080
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Installs Python dependencies.
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copies and installs roostercore.
COPY core/pyproject.toml /app/core/
COPY core/roostercore/ /app/core/roostercore/
RUN pip install --no-cache-dir ./core

# Copies src.
COPY src/ /app/src/

# Runs the server.
EXPOSE 8080
CMD ["python", "src/main.py"]
