from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ListingDetailView
from .views import ListingCreateView

app_name = 'store'
urlpatterns = [
    path('', views.store, name='store'),
    path('listing/<int:pk>/', ListingDetailView.as_view(), name='listing_detail'),
    path('listing/create/', ListingCreateView.as_view(), name='listing_create'),
    path('create/', views.create_listing, name='create_listing')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
