from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ListingDetailView
app_name = 'store'
urlpatterns = [
    path('', views.store, name='store'),
    path('store/', views.store, name='store'),
    path('listing/<int:pk>/', ListingDetailView.as_view(), name='listing-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
