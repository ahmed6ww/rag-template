# Dockerfile for Streamlit
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

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run Streamlit when the container launches
CMD ["streamlit", "run", "streamlit_app.py", "--server.port", "8501"]
