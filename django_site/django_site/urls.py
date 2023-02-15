"""django_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from store.views import login_view_custom, logout_view, SearchListingView, password_change, register



class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

urlpatterns = [
    path('', include('store.urls')),
    path('admin/', admin.site.urls),
    path('login/', login_view_custom, name='login'),
    path('accounts/login/', login_view_custom, name='login_reg'),
    path('change_password/', password_change, name='password_change'),
    path('logout/change_password/', password_change, name='change_password'),
    path('change_password_done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('search/', SearchListingView, name='search_listing'),
]