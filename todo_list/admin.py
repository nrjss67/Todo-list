from django.contrib import admin

from todo_list.models import Tag, Task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    
    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "deadline", "is_done")