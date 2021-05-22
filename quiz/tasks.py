from celery import shared_task

@shared_task
def count():
    for i in range(3):
        print(i*2)
