from fastapi import FastAPI

from api import endpoints
from worker.celery_config import celery_app

app = FastAPI()


celery_app = celery_app
app.celery_app = celery_app

app.include_router(endpoints.router)


# Health check route
@app.get("/ping")
def ping():
    return {"ping": "pong!"}
