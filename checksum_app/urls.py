from django.urls import path
from .views import checksum_view

urlpatterns = [
    path('', checksum_view, name='checksum'),
]
