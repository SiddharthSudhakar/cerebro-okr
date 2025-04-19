

## Getting Started

### Backend
```cd backend
uv run app\seed.py
uv run fastapi dev --app app```

### Backend on Docker
``cd backend
docker build . -t cerebro-okr-backend --no-cache
docker run cerebro-okr-backend```