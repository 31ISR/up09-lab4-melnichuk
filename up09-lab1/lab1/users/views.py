from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Create your views here.
def register_view(req):

    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form = UserCreationForm()
    return render(req,'users/register.html', {'form':form})

def login_view(req):
    
    if req.method == "POST":
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            login(req, form.get_user())
            return redirect("posts:list")
    else:
        form = AuthenticationForm()
    return render(req,'users/login.html', {'form':form})