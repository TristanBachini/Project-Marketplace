from django.shortcuts import render
from login_app.forms import UserForm

# Create your views here.
def login(request):
    return render(request, "login_app/login.html")

def register(request):
    form = UserForm()
    data = {"form":form}
    if(request.method=='POST'):
        form = UserForm(request.POST)
        if form.is_valid:
            print("valid naman")
        else:
            print(form.errors)
    return render(request, "login_app/register.html",data)