from celery import Celery
from celery.schedules import crontab

from celery.task import periodic_task
from .amc_task import amcSms

app = Celery()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )



# @periodic_task(run_every=(crontab(minute='*/1')), name="my_first_task")
# # @periodic_task(run_every=(timedelta(seconds=40)), name="my_first_task")
# def my_first_task():
#     print("This is my first task")


@app.task
def test(arg):
    print(arg)


app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}
app.conf.timezone = 'Asia/Kolkata'




def test(args):
    print(args)


@app.task
def call():
    a = amcSms()
    return a
