from fastapi import FastAPI
from fastapi.responses import JSONResponse
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="CareCloud DevOps Challenge")

Instrumentator().instrument(app).expose(app)

@app.get("/")
def root():
    return {
        "application": "CareCloud DevOps Challenge",
        "status": "running"
    }

@app.get("/health")
def health():
    return JSONResponse(
        {
            "status": "healthy"
        }
    )
