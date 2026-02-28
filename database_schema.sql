CREATE TABLE jobs (
    job_id UUID PRIMARY KEY,
    cron_expression VARCHAR(100),
    payload JSONB,
    status VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE job_executions (
    execution_id UUID PRIMARY KEY,
    job_id UUID REFERENCES jobs(job_id),
    execution_time TIMESTAMP,
    status VARCHAR(20),
    retry_count INT DEFAULT 0,
    error_message TEXT
);
