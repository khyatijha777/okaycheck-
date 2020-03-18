from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse
# Create your views here.
def user_login(req):
    if req.method=="POST":
        if req.session.test_cookie_worked():
            req.session.delete_test_cookie()
            username = req.POST['username']
            password = req.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(req, user)
                    return redirect("home")
        else:
            return HttpResponse("enable cookies and try again")
    #checking if the browser supports cookies
    req.session.set_test_cookie()
    return render(req, 'accounts/login.html')
def register(req):
    if req.method == 'POST':
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        user_name = req.POST['user_name']
        email= req.POST['email']
        p1 = req.POST['password']
        p2 = req.POST['password2']
        #check if paswrd match
        if p1==p2:
            if not User.objects.filter(username=user_name).exists():
                if not User.objects.filter(email=email).exists():

                    user = User.objects.create_user(username=user_name, email=email, first_name=first_name, last_name=last_name, password=p1)
                    user.save()
                    return redirect("home")
        

    
    
    return render(req, 'accounts/register.html')
def dashboard(req):
    return render(req,'home/home.html')
def user_logout(req):
    if req.method =="POST":
        logout(req)
    return render(req, 'home/home.html')