# scheduler - narzędzie do cyklicznego wykonywania zadań
# cron, harmonogram zadań
import time

from apscheduler.schedulers.blocking import BlockingScheduler


def job():
    print("Wykonanie zaplanowanego zadania")
    time.sleep(1)


scheduler = BlockingScheduler()

# konfiguracja
# scheduler.add_job(job, 'interval', minutes=1)
scheduler.add_job(job, 'interval', seconds=5)
# scheduler.add_job(job, 'cron', hour=3, minute=0)
# scheduler.add_job(job, 'date',run_date="2025-12-25 12:00:00")

# uruchomienie
scheduler.start()
# +-----------------------+----------------------------------------------+
# | Parametr              | Znaczenie                                    |
# +-----------------------+----------------------------------------------+
# | id                    | Unikalny identyfikator joba                  |
# | name                  | Opisowy label / nazwa joba                  |
# | max_instances         | Maksymalna liczba równoległych uruchomień   |
# | coalesce              | Nadrabia opóźnienia jednym wykonaniem       |
# | misfire_grace_time    | Tolerancja spóźnienia (w sekundach)         |
# | replace_existing      | Nadpisuje job o tym samym ID                |
# +-----------------------+----------------------------------------------+
