from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
def profile(request):
    '''return profile'''
    return render(request, 'user_profile/basic_table.html')


def edit_user(req):
    if req.method=="POST":
        username = req.POST['username']
        first_name = req.POST['first_name']
        last_name = req.POST['last_name']
        email = req.POST['email']
        user_id = req.user.id
        the_user = User.objects.get(id=user_id)
        the_user.username =username
        the_user.first_name =first_name
        the_user.last_name =last_name
        the_user.email =email
        the_user.save()
        return redirect("home")



    curr_user = req.user
    return render(req, 'user_profile/edit_user.html', {"user":curr_user})
