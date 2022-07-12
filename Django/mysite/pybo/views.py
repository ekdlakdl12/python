from django.shortcuts import render
from django.http import HttpResponse

def index(request): #request값이 사용되지 않아 밑줄나옴
    return HttpResponse("안녕하세요 pybo 오신것을환영합니다")

