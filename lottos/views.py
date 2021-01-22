from django.shortcuts import render
from django.http.response import HttpResponse
import random
# Create your views here.
def index(request) :
    num = request.GET.get('num','')
    print(num)
    if len(num) < 1 :
        return HttpResponse("<h1>파라미터가없습니다</h1>")
    if request.method == 'GET':
        lotto = []
        while len(lotto) < 6:
            lotto.append(random.randint(1,46))
            lotto=list(set(lotto))
            return HttpResponse(f"<h1>번호추천 : {lotto}</h1>")
    return HttpResponse("post")
