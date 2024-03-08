# Use the official Python image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project directory into the container
COPY . .

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
