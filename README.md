# ⏰ Distributed Job Scheduler

> Day 6 – High Scale Backend Systems

---

## 📌 Problem Statement

Design a distributed job scheduler system like:

- Cron (but distributed)
- Background job systems
- Task schedulers in microservices

The system should:
- Allow users to schedule jobs
- Support cron expressions
- Execute jobs reliably
- Retry failed jobs
- Work in distributed environments

---

# 🎯 Functional Requirements

- Create scheduled jobs
- Define cron expression
- Execute jobs at correct time
- Retry on failure
- Track job status

---

# ⚙️ Non-Functional Requirements

- High availability
- Exactly-once or at-least-once execution
- Horizontally scalable
- Fault tolerant
- Support millions of scheduled jobs

---

# 🧠 High-Level Architecture

Client/API
     ↓
Scheduler Service
     ↓
Job Queue
     ↓
Worker Nodes
     ↓
Database

---

# 🧠 Core Design Decisions

✔ Separate scheduler and workers  
✔ Use message queue for decoupling  
✔ Store job metadata in DB  
✔ Track execution history  

---

# 🚀 Advanced Concepts Used

- Leader Election
- Distributed Locks
- Job Queuing
- Retry Strategy
- Idempotency

---

⭐ Designed for Senior Backend Interviews
