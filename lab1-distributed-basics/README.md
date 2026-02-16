# **Distributed Systems: Architecture, Paradigms, Implementation, and Security**

This course introduces the principles, architectures, and paradigms of distributed systems. Students will design, implement, observe, and secure real-world distributed applications using modern tools. The course emphasizes **hands-on labs**, **system thinking**, **failure handling**, **scalability**, **machine learning pipelines**, and **security in distributed environments**.


**Lab Objectives**

- Run a **multi-service distributed system**
    
- Understand **what makes a system “distributed”**
    
- Observe **latency, partial failure, and service dependency**
    
- Experience **why distributed systems are hard**
    
- Use **Docker + Docker Compose** as the base platform for the course

**What is a Distributed System?**
A system where:

- Multiple **independent processes**
    
- Running on **different machines or containers**
    
- Communicate via **network calls**
    
- Can **fail independently**

**Problems We Will See Today**


|Problem|Meaning|
|---|---|
|Latency|Network calls are slow|
|Partial failure|One service dies, others stay alive|
|Dependency|One service depends on another|
|Non-atomicity|Not everything fails together|

Docker

## Tools Used in Lab 1

- Docker
    
- Docker Compose
    
- Python + FastAPI
    
- PostgreSQL
    
- curl / Postman

## Folder Structure (MANDATORY)

```text
lab1-distributed-basics/
│
├── api/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── worker/
│   ├── worker.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── db/
│   └── init.sql
│
├── docker-compose.yml
└── README.md
```

Each folder = **independent service**  
Each service can fail **alone**

## Step 1 — API Service

### API Responsibilities

- Receive HTTP request
    
- Store request in DB
    
- Call worker service

DEMO

- `db` and `worker` are **service names**, not localhost
    
- Network call introduces **latency**
    
- DB is a **remote dependency**

## Step 2 — Worker Service

### Worker Responsibilities

- Simulate processing delay
    
- Return result

DEMO

## Step 3 — Database Initialization

### `db/init.sql`
## Step 4 — Docker Compose 

### `docker-compose.yml`


## Step 5 — Run the System


`docker compose up --build`

Test:

`curl http://localhost:8080/process`

Expected output:

`{   "worker_response": {"status": "done"},   "latency_seconds": 2.01 }`


## Step 6 — Failure Experiments 

### Experiment 1 — Kill Worker

`docker compose stop worker`

Call API again:

`curl http://localhost:8080/process`

Discuss:

- API is alive
    
- Worker is dead
    
- System partially fails
### Experiment 2 — Kill Database

`docker compose stop db`

Observe:

- API crashes or throws error
    
- Worker still alive


```bash
docker compose up --build

curl http://localhost:8080/process

docker compose stop worker

curl http://localhost:8080/process

docker compose start worker

docker compose stop db

curl http://localhost:8080/process

docker compose start db

