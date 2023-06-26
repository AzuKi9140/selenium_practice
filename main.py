import os
import time
from datetime import datetime

import schedule
from dotenv import load_dotenv

from src.screenshot import screenshot

load_dotenv(override=True)


def job():
    screenshot(datetime.now())


if os.getenv("DEVELOP"):
    schedule.every().minute.do(job)
else:
    schedule.every().hour.at(":55").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
