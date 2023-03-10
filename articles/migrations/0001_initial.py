# Generated by Django 4.1.6 on 2023-02-12 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('figures', '0001_initial'),
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issn', models.CharField(max_length=9)),
                ('journal_title', models.TextField()),
                ('article_title', models.TextField()),
                ('volume', models.IntegerField(null=True)),
                ('issue', models.IntegerField(null=True)),
                ('date', models.DateField(null=True)),
                ('authors', models.ManyToManyField(to='authors.author')),
                ('figures', models.ManyToManyField(to='figures.figure')),
            ],
        ),
    ]
