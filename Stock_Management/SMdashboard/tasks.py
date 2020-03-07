from __future__ import absolute_import, unicode_literals
from celery import shared_task

from celery.task import periodic_task
from celery.schedules import crontab
from datetime import timedelta


@periodic_task(run_every=(crontab(minute='*/1')), name="my_first_task")
# @periodic_task(run_every=(timedelta(seconds=40)), name="my_first_task")
def my_first_task():
    print("This is my first task")

