import random
import time

class Worker:

    def execute(self, job_id):
        print(f"Executing {job_id}")
        time.sleep(2)

        if random.choice([True, False]):
            raise Exception("Random failure")

        print(f"{job_id} completed")


if __name__ == "__main__":
    worker = Worker()
    try:
        worker.execute("email_job_101")
    except Exception as e:
        print("Retry logic triggered:", e)
