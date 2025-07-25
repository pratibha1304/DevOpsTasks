# Use official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy files to container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set default command to run your script
CMD ["python", "app.py"]

