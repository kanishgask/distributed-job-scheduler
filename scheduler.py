import time
import threading
from queue import PriorityQueue
from datetime import datetime, timedelta

class ScheduledJob:
    def __init__(self, job_id, run_at, function):
        self.job_id = job_id
        self.run_at = run_at
        self.function = function

    def __lt__(self, other):
        return self.run_at < other.run_at


class JobScheduler:
    def __init__(self):
        self.job_queue = PriorityQueue()
        self.running = False

    def schedule(self, job_id, delay_seconds, function):
        run_time = datetime.now() + timedelta(seconds=delay_seconds)
        job = ScheduledJob(job_id, run_time, function)
        self.job_queue.put(job)

    def start(self):
        self.running = True
        threading.Thread(target=self._run, daemon=True).start()

    def _run(self):
        while self.running:
            if not self.job_queue.empty():
                job = self.job_queue.queue[0]
                if datetime.now() >= job.run_at:
                    self.job_queue.get()
                    try:
                        job.function()
                    except Exception as e:
                        print(f"Job {job.job_id} failed:", e)
            time.sleep(1)


# Example
if __name__ == "__main__":
    scheduler = JobScheduler()
    scheduler.start()

    scheduler.schedule("job1", 5, lambda: print("Job executed!"))
    time.sleep(10)
