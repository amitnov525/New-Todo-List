from django.contrib import admin
from django.contrib import admin
from main.models import Task
# Register your models here.
@admin.register(Task)
class DisplayTask(admin.ModelAdmin):
    list_display=['user','title','description','completed','created_at']
