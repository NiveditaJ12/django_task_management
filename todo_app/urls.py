from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:id>',views.change_task, name='change_task'),
    path('delete/<int:id>',views.remove_task, name='remove_task'),
]