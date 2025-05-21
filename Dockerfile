# 1. Base image
FROM python:3.11-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set working directory
WORKDIR /app

# 4. Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# 5. Copy project files
COPY . .

# 6. Expose port
EXPOSE 8000

# 7. Default command
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "courier_management_backend.wsgi:application"]

