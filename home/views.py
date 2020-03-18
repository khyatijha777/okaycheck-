from django.shortcuts import render,redirect
# from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import ToDo
from datetime import date
import datetime 

current_time = datetime.datetime.now().strftime("%H:%M:%S")
''' main page that return todo list'''
def home(req):
    '''home function'''
    if req.method=="POST":
        u_id = req.user
        date_created = datetime.date.today()
        time_created = datetime.datetime.now().strftime("%H:%M:%S")
        complete_by_date = req.POST['complete_by_date']
        complete_by_time = req.POST['complete_by_time']
        data= req.POST['data']
        done = False
        task = ToDo(u_id=u_id, date_created=date_created, time_created=time_created, complete_by_date=complete_by_date,data=data, complete_by_time=complete_by_time, done=done)
        task.save()
        return redirect('home')
    else:
        data = ToDo.objects.all().filter(u_id = req.user.id)
        date_today = datetime.date.today()
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        
        todo_data = {'data':data, 'date_today':date_today, 'time_now':time_now}
        return render(req, 'home/home.html', todo_data)
 
def delete_task(req, task_id):
    if req.method=="GET":
        task = ToDo.objects.all().filter(todo_id=task_id)
        task.delete()
        return redirect('home')
#  view to edit the task which is a future scope
# def edit_task(req, task_id):
#     if req.method=="GET":
#         task = ToDo.objects.all().filter(todo_id=task_id)
#         task.delete()
#         return redirect('home')