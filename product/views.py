from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def product(request):
    return HttpResponse(template.render())
template=loader.get_template('myfirst.html')
