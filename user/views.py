from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import User
# Create your views here.
def login(request):
    if request.method == "POST":
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        data = {}
        if not ( userid and password):
            data['error'] = '모든 값을 입력해주세요.'
            return render(request, 'login.html', data)
        else:
            user = User.objects.get(userid=userid)
            if user.password == password:
                request.session['user'] = userid
                return redirect('main')
            else:
                data['error'] = '아이디 혹은 비밀번호가 틀립니다.'
                return render(request, 'login.html', data)
    else:
        return render(request,'login.html')

def register(request):
    if request.method == "POST" :
        userid = request.POST.get('userid')
        username = request.POST.get('username')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        data = {}
        if not ( userid and username and password and gender) :
            data['error'] = '모든 값을 입력해주세요.'
            return render(request, 'register.html', data)
        else :
            user = User(userid=userid, username=username, password=password, gender=gender)
            user.save()
            return redirect('main')
    else :
        return render(request,'register.html')

def ttt(request) :
    context ={'loop_for' : range(1,32)}
    return render(request,'0119_5.html',context)

def detail(request, question_id):
    return HttpResponse(f"you're {question_id} looking at question {queistion_id}")

def results(request, question_id):
    response="you're looking at the results of question %s %s."
    return HttpResponse(response % (question_id, question_id))

def main(request):
    return render(request, 'main.html')

