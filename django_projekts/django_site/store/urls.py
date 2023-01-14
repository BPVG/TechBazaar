from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'store'
urlpatterns = [
    path('', views.store, name='store'),
    path('store/', views.store, name='store'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)