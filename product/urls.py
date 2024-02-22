from django.urls import path
from . import views

urlpatterns = [
    path('product/details/<int:id>', views.details, name='details')
]
