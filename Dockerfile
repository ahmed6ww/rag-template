# Dockerfile for FastAPI
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Install Poetry
RUN pip install poetry

# Set the working directory in the container
WORKDIR /app

# Copy pyproject.toml and poetry.lock
COPY pyproject.toml poetry.lock /app/

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install 

# Copy the entire project
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Run FastAPI when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
