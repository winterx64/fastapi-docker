import redis
from fastapi import FastAPI

app = FastAPI()
r = redis.Redis(host="redis", port=6379)

@app.get("/")
def root():
    return {"redis": r.ping()}
