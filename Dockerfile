# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 🔥 Create data directory and give permissions
RUN mkdir -p /app/data && chmod -R 777 /app/data

# Expose Flask port
EXPOSE 3000

# Run Flask app
CMD ["python", "app.py"]