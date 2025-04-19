from fastapi import FastAPI
from .routers import goals, key_results, employees, allocations, kpis
import toml

app = FastAPI()


with open("pyproject.toml", "r") as f:
    pyproject = toml.load(f)
APP_VERSION = pyproject.get("project", {}).get("version", "unknown")

@app.get("/version")
def get_version():
    return {"version": APP_VERSION}


app.include_router(goals.router)
app.include_router(key_results.router)
app.include_router(employees.router)
app.include_router(allocations.router)
app.include_router(kpis.router)
