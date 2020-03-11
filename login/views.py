from django.shortcuts import render
from django.http import HttpResponseRedirect
# from django.http import HttpResponse
from .models import Login
# from .forms import registration_form
# # Create your views here.

# def get_user_info(request):
#     if request.method == 'POST':
#         form = registration_form(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('register')
#     else:
#         form = registration_form()
#         return render(request, 'login/register.html',{'form':form})
def login(request):
    # user =  Login.objects.all()
    # user_info = {'user': user}
    # user = request.user.get_profile()
    return render(request, 'login/login.html')

def register(request):
    return render(request, 'login/register.html')