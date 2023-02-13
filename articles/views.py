from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.


def list_articles(request):
    template = loader.get_template('articles.html')
    return HttpResponse(template.render())
