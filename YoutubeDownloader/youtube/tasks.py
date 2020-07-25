from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import TempDir


@shared_task
def clear_dir():
    print('Clearing disk... ')


@shared_task
def insert_info(path):
    TempDir(path=path).save()
    print('Inserted Temp directory in DB')
