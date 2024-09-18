# Dockerfile

# Copyright 2024 Qi Tianshi. All rights reserved.


# Set up environment
FROM python:3.10-slim
ENV PORT=8080
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Python dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy src
COPY src/ /app

# Run app
EXPOSE 8080
CMD ["python", "main.py"]
