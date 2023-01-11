from django.http import HttpResponse
from django.template import loader

def store(request):
  template = loader.get_template('alllistings.html')
  return HttpResponse(template.render())

def show_side_menu(request):
    show_menu = request.path.startswith("/menu")  # check the request's path
    return render(request, 'alllistings.html', {'show_menu': show_menu})