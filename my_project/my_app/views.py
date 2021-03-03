from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def result(request):
    first = str(request.POST['firstname'])
    last = str(request.POST['lastname'])
    Reg = int(request.POST['register'])
    Dep = str(request.POST['department'])
    mobile = int(request.POST['mobile'])
    return render(request,"result.html", {"firstname":first,"lastname":last,"register":Reg, "department": Dep, "mobile":mobile})
