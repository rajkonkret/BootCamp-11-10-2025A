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
# Parametr
# Znaczenie
# id
# unikalny identyfikator
# name
# opisowy label
# max_instances
# limit równoległych uruchomień
# coalesce
# nadrabia opóźnienia jednym runem
# misfire_grace_time
# tolerancja spóźnienia
# replace_existing
# nadpisuje job o tym samym ID
