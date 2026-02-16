from fastapi import FastAPI
import time
import os

app = FastAPI()

SLEEP_SECONDS = float(os.getenv("SLEEP_SECONDS", "2"))

@app.get("/work")
def work():
    time.sleep(SLEEP_SECONDS)  # simulate processing latency
    return {"status": "done", "slept_seconds": SLEEP_SECONDS}
