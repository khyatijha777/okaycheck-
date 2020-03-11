from django.contrib import admin
from home.models import ToDo
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['todo_id', 'u_id', 'data', 'complete_by_date', 'complete_by_time', 'done']
    list_display_links = ['data', 'todo_id', 'u_id']
    list_editable = ['done']
    list_per_page = 10
    # search_fields = ['u_id', 'todo_id', 'data']
admin.site.register(ToDo, ToDoAdmin)
