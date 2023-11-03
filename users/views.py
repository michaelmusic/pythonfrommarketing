from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
#old code hello world
# def users(request):
#     return HttpResponse("Hello world!")

# New Code which renders our first HTMl template from the template folder


def users(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

