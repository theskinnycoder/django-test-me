from django.urls import path

from .views import create_classroom, get_classroom

urlpatterns = [
    path('create/', create_classroom, name='create_classroom'),
    path('<int:id>/', get_classroom, name='get_classroom'),
]
