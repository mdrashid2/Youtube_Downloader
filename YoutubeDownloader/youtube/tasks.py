# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .models import TempDir


@shared_task
def clear_dir(path):
    print('Deleting Temp folder : ',path)