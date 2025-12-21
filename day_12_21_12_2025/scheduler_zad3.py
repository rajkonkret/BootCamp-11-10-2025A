import logging
import time
from logging.handlers import TimedRotatingFileHandler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

# konfiguracja loggera
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# konfiguracja rotowania plików
file_handler = TimedRotatingFileHandler(
    filename="jobs.log",
    when="midnight",
    interval=1,
    backupCount=7,
    encoding='utf-8'
)

file_handler.setFormatter(
    logging.Formatter("%(asctime)s %(levelname)s %(message)s")
)
logger.addHandler(file_handler)

# opcjonalnie StreamHandler - by widziec logi w konsoli
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(
    logging.Formatter("%(asctime)s %(levelname)s %(message)s")
)
logger.addHandler(stream_handler)


def job_listener(event):
    job_id = event.job_id
    if event.exception:
        logger.error(f"Job {job_id} zakończone błędem: {event.exception!r}")
    else:
        logger.info(f"Job {job_id} wykonany pomyslnie")


def my_job():
    time.sleep(1)
    return "wynik"
