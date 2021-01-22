from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import Charac
# Create your views here.
def novel(request, cname1, cname2):
    context = {'name1':cname1, 'name2':cname2}
    return render(request, 'novel_.html',context)
