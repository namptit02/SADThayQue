# urls.py trong ứng dụng "search"
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
]
