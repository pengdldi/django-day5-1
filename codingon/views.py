from django.shortcuts import render
from .models import testU
# Create your views here.
def signup(request) :
    if request.method == "POST" :
        post = request.POST
        data = {
            'username':post.get('username'),
            'gender':post.get('gender'),
            'birth_1':post.get('birth_1'),
            'birth_2':post.get('birth_2'),
            'birth_3':post.get('birth_3')
        }
        return render(request, 'receive.html', data)
    else :
         return render(request,'signup_test.html')
