from fastapi import FastAPI

app = FastAPI()

# Health check route
@app.get("/ping")
def ping():
    return {"ping": "pong!"}