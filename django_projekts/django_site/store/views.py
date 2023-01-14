from django.shortcuts import render
from .models import Listing

def store(request):
    object_list = Listing.objects.filter(statuscompleted = False)
    return render(request, 'alllistings.html', {'object_list': object_list})

def show_side_menu(request):
    show_menu = request.path.startswith("/menu")  # check the request's path
    return render(request, 'alllistings.html', {'show_menu': show_menu})