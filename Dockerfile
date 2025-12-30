# Dockerfile
FROM python:3.10-slim

# Create non-root user (security best practice)
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# Set working directory
WORKDIR /app

# Copy application
COPY app.py .

# Run the app
CMD ["python", "app.py"]
