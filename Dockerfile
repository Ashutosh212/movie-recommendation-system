# Use official Python image with Python 3.12
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (optional: for streamlit or other packages)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install pip and poetry (for pyproject.toml support)
RUN pip install --upgrade pip \
    && pip install --no-cache-dir uv \
    && uv pip install -r <(uv pip compile pyproject.toml --generate-hashes)

# Expose port for Streamlit (default 8501) and FastAPI (8000)
EXPOSE 8501
EXPOSE 8000

# Default command (can be overridden)
CMD ["streamlit", "run", "frontend/app.py"]

