from django.db import models

class TempDir(models.Model):
    pk_dir = models.AutoField(primary_key=True)
    path  = models.FilePathField()
    created = models.DateTimeField(auto_now=True)

