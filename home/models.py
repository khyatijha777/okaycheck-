from django.db import models
from login.models import Login
# Create your models here.
'''COnatins list to tasks'''
class ToDo(models.Model):
    todo_id =  models.AutoField(primary_key=True)
    date_created = models.DateField()
    time_created =  models.TimeField()
    data = models.TextField(blank = True)
    done = models.BooleanField()
    complete_by_date = models.DateField(auto_now=False, auto_now_add=False)
    complete_by_time = models.TimeField(auto_now=False, auto_now_add=False)
    u_id = models.ForeignKey(Login, on_delete=models.CASCADE)
    def __str__(self):
        return self.data[:12]
        