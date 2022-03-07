from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/destroy/<int:id>', views.delete_curso, name='destroy'),
]
