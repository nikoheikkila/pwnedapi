from django.urls import path
from .views import pwnedapi_view

urlpatterns = [
    path('pwnedapi/', pwnedapi_view, name='pwnedapi')
]
