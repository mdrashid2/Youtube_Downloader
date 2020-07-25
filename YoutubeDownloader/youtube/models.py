from django.db import models

class TempDir(models.Model):
    path  = models.FilePathField()
    created = models.DateTimeField(auto_now=True)

