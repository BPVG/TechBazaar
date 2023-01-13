from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Listing

def store(request):
  template = loader.get_template('alllistings.html')
  object_list = Listing.objects.filter(statuscompleted = False)
  return render(request, 'existing_template.html', {'object_list': object_list})

def show_side_menu(request):
    show_menu = request.path.startswith("/menu")  # check the request's path
    return render(request, 'alllistings.html', {'show_menu': show_menu})