from celery import shared_task

from .models import Website


@shared_task
def add_to_db():
    print("celery run")
    w = Website(name="Celery")
    w.save()
    pass
