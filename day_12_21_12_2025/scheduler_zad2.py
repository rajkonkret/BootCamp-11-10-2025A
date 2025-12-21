import logging
import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

# _levelToName = {
#     CRITICAL: 'CRITICAL',
#     ERROR: 'ERROR',
#     WARNING: 'WARNING',
#     INFO: 'INFO',
#     DEBUG: 'DEBUG',
#     NOTSET: 'NOTSET',
# }

# konfiguracja loggera
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


# definicja listenera
def job_listener(event):
    job_id = event.job_id
    if event.exception:
        logger.error(f"Job {job_id} zakończone błędem: {event.exception!r}")
    else:
        logger.info(f"Job {job_id} wykonany pomyslnie")


def my_job():
    time.sleep(1)
    return "wynik"


# konfiguracja schedulera i listenera
scheduler = BackgroundScheduler()  # wykonuje zadania w nowym wątku

# podłaczenie listenera pod eventy
scheduler.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)  # | -> or

# dodanie zadania do schedulera
scheduler.add_job(my_job, 'interval', minutes=1, id="interval_job")

scheduler.start()

# podtrzymywanie procesu (demo)
# podtrzymywanie procesu (demo) - tak aby głowny wątek nadal istniał
# koniec głównego wątku oznacza koniec wątku schedulera
try:
    while True:
        time.sleep(5)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
