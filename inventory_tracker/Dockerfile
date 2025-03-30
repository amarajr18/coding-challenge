# Use official Python base image
FROM python:3.11-slim

# Set working directory in the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Default command: run main.py with input.txt
CMD ["python", "main.py", "input.txt"]
