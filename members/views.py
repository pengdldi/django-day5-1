from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def test(request):
    return HttpResponse("<h2>Test Page</h2>")

def test2(request):
    return HttpResponse("<h2>Test2</h2>")

def signup(request):
    if request.method == 'POST' :
        username=request.POST['username']
        email=request.POST['email']
     # if username == 'exit' :
     #   return HttpResponse("<h2>나가기</h2>")
     # elif username == 'codingon':
      #    return render(request,'login.html')
     # else :
        member = Members(
             username=username,
             useremail=email
        )
        member.save()
        res_data={}
        res_data['res']='등록성공'
        return render(request, 'index.html', res_data)
    return render(request,'index.html')
