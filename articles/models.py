from django.db import models

from authors.models import Author
from figures.models import Figure


class Article(models.Model):

    issn = models.CharField(max_length=9)
    journal_title = models.TextField()
    article_title = models.TextField()
    volume = models.IntegerField(null=True)
    issue = models.IntegerField(null=True)
    date = models.DateField(null=True)

    figures = models.ManyToManyField(Figure)
    authors = models.ManyToManyField(Author)

    class Meta:
        db_table = 'articles'
