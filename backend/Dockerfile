FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN apt-get update && apt-get install -y curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh

# Copy project files
COPY backend/pyproject.toml backend/uv.yaml /app/
COPY backend/app /app/app
COPY backend/app/seed.py /app/seed.py
COPY backend/.venv /app/.venv

# Activate the prebuilt virtualenv
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Optional: install system deps for common wheels
RUN apt-get install -y build-essential libpq-dev

# Launch app
CMD ["sh", "-c", "python /app/seed.py && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
