from django.shortcuts import render
# from django.http import HttpResponse
from .models import ToDo


''' main page that return todo list'''
def home(req):
    '''home function'''
    data = ToDo.objects.all()
    todo_data = {'data':data}
    return render(req, 'home/home.html', todo_data)
 