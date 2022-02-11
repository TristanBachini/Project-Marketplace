from django.shortcuts import render
from login_app.forms import UserForm

# Create your views here.
def login(request):
    form = UserForm()
    data = {"form":form}
 
    return render(request, "login_app/login.html",data)

def trying(request):
    return render(request, "login_app/try.html")