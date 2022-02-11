from django.shortcuts import render

# Create your views here.
def home(request):
    m = 1
    data ={"number":m}
    return render(request,"main/home.html",data)
