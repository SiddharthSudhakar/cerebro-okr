FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN apt-get update && apt-get install -y curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh

# Add uv to PATH
ENV PATH="/root/.local/bin:$PATH"

# Copy project files
COPY app/ /app/app/
COPY app/routers/ /app/app/routers/

COPY pyproject.toml /app/pyproject.toml
COPY .python-version /app/.python-version
COPY uv.lock /app/uv.lock

# Create a virtual environment
RUN python -m venv /app/.venv

# Activate the virtual environment
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Optional: install system deps for common wheels
# RUN apt-get install -y build-essential libpq-dev
# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*


# Expose port 8000
EXPOSE 8000

# Launch app
#CMD ["sh", "-c", "cd app/ && uv run app/seed.py && uv run fastapi dev --app app"]
CMD ["uv", "run", "uv run app/seed.py &&","fastapi", "dev", "--app", "app.main:app"]