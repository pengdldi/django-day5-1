from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import Members
# Create your views here.
def login_after(request) :
    return HttpResponse("세션읽기& 세션 없으면 리다이렉션")

def login(request):
    print(dir(request))
    if request.method== 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)

        err = {}

        if not (useremail and username) :
            err['err'] = '유효성이 잘못되었습니다.'
            return render(request, 'login.html', err)
        else :
            member = Members.objects.get(username=username)

            if useremail == member.useremail :
                request.session['user'] = member.id
                return redirect('/members')
        # err = {}
        # if not(username and email) : 
        #     err['err'] ='비밀번호 오류'
        #     return  render(req, 'login.html', err)
        # else :
            ## db read
            ## session 만들기

        return redirect(f"<h1>{member.useremail}</h1>")

def index(request):
    #print(dir(req))
    print(request.GET.get('id',''))
    num = request.GET.get('id','') 
    if len(num) < 1:
        return HttpResponse("<h1>version 1 : dynamic page</h1>")

def gu(request) :
    num =  request.GET.get('num','')
    return HttpResponse(f'<h1>gugu: {num_gugu(num)}</h1>')

def num_gugu(num):
    str=""
    for i in range(9):
        str+=f"{int(num)}*{i+1}={int(num)*(i+1)}<br>"
    return str

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
