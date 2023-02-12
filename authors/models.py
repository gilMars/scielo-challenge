from django.db import models


class Author(models.Model):
    surname = models.TextField()
    name = models.TextField()
    contrib_id = models.TextField(unique=True)

    class Meta:
        db_table = 'authors'
