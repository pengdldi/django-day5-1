from django.shortcuts import render
from django.http.response import HttpResponse
import random
# Create your views here.
def index(request) :
    lotto = []
    while len(lotto) < 6:
        lotto.append(random.randint(1,46))
        lotto=list(set(lotto))
    return HttpResponse(f"<h1>번호추천 : {lotto}</h1>")
