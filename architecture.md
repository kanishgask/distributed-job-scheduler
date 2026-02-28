# 🏗️ Distributed Scheduler Architecture

Client
   ↓
API Service
   ↓
Scheduler Cluster (Leader Election)
   ↓
Message Queue (Kafka/RabbitMQ)
   ↓
Worker Cluster
   ↓
Database (Sharded + Replication)

---

# Component Explanation

## Scheduler Cluster
- Only leader schedules jobs
- Uses distributed lock
- Avoids duplicate execution

## Message Queue
- Decouples scheduler from workers
- Ensures retry & durability

## Worker Cluster
- Pulls tasks
- Executes jobs
- Updates execution status

## Database
- Stores job metadata
- Stores execution history
- Indexed on execution time

---

# Scaling Strategy

- Partition jobs by hash(job_id)
- Multiple scheduler instances
- Queue partitions for parallelism
- Stateless workers

---

# Failure Handling

If scheduler crashes:
- New leader elected
- Pending jobs recovered from DB

If worker crashes:
- Message re-queued
- Retry logic triggered
