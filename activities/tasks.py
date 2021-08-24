from time import sleep

from celery.task import task

@task
def send_email(username):
    sleep(10)
    print("email send to {}".format(username))
