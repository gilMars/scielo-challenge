from django.db import models


class Figure(models.Model):
    label = models.TextField()
    title = models.TextField()
    url = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        db_table = 'figures'

