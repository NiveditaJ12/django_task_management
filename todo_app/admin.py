from django.contrib import admin # type: ignore
from .models import ToDoModel, StartTime

admin.site.register(ToDoModel)
admin.site.register(StartTime)
