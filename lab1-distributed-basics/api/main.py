from fastapi import FastAPI
import psycopg2
import requests
import time
import os

app = FastAPI()

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "labdb")
DB_USER = os.getenv("DB_USER", "labuser")
DB_PASS = os.getenv("DB_PASS", "labpass")

WORKER_URL = os.getenv("WORKER_URL", "http://worker:8001/work")


def insert_log(message: str) -> None:
    conn = psycopg2.connect(
        host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
    )
    cur = conn.cursor()
    cur.execute("insert into logs(message) values (%s)", (message,))
    conn.commit()
    cur.close()
    conn.close()


@app.get("/process")
def process():
    # 1) store a log in DB
    insert_log("request received by api")

    # 2) call worker and measure latency
    start = time.time()
    r = requests.get(WORKER_URL, timeout=10)
    latency = time.time() - start

    insert_log(f"worker called, latency={latency:.3f}s")

    return {
        "api": "ok",
        "worker_status": r.json(),
        "latency_seconds": round(latency, 3),
    }
