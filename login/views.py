from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(req):
    return render(req, 'login/login.html')