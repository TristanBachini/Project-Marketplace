from django.shortcuts import render
from login_app.forms import UserForm

# Create your views here.
def login(request):
    return render(request, "login_app/login.html")

def register(request):
    form = UserForm()
    data = {"form":form}
    return render(request, "login_app/register.html",data)