from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members
# Create your views here.
def gu(request) :
    num =  request.GET.get('num','')
    return HttpResponse(f'<h1>gugu: {num_gugu(num)}</h1>')

def num_gugu(num):
    str=""
    for i in range(9):
        str+=f"{int(num)}*{i+1}={int(num)*(i+1)}<br>"
    return str

def index(request):
    return HttpResponse("version1")

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
