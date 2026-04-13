# Stage 1: Build stage
FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user -r requirements.txt


# Stage 2: Runtime stage
FROM python:3.10-slim

WORKDIR /app

# Copy installed dependencies from builder
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY . .

# Set path
ENV PATH=/root/.local/bin:$PATH

CMD ["python", "app.py"]