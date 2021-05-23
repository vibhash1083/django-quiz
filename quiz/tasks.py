from celery.decorators import task

@task
def count():
    for i in range(3):
        print(i*2)
