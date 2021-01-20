from django.shortcuts import render
from .models import User
# Create your views here.
def register(request):
    users = User.objects.order_by('registered')
    return render(request,'register.html', {'users':users})

def ttt(request) :
    return render(request,'0119_2.html',{})
