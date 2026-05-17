from apscheduler.schedulers.blocking import BlockingScheduler
import os

scheduler = BlockingScheduler()

scheduler.add_job(
    lambda: os.system(
        "python pipeline/run_pipeline.py"
    ),
    "interval",
    days=1
)

print("Scheduler running...")

scheduler.start()