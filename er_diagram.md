# 📊 ER Diagram - Job Scheduler

JOBS
- job_id (PK)
- cron_expression
- payload
- status
- created_at

JOB_EXECUTIONS
- execution_id (PK)
- job_id (FK)
- execution_time
- status
- retry_count
- error_message

Relationship:
Job 1 → N Job Executions
