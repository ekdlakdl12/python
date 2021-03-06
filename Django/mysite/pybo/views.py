from django.http import HttpResponse
from .models import Question #db임포트
from django.shortcuts import render, get_object_or_404, redirect  # render 함수는 파이썬 데이터를 템플릿에 적용한 HTML을 반환하는 함수이다.
from django.utils import  timezone

def index(request): #request값이 사용되지 않아 밑줄나옴
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date') #- 는 역순출력임
    context = {'question_list':question_list}
    return render(request,'pybo/question_list.html',context)

def detail(request, question_id):
    """
    pybo 내용 출력

    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)
    """
    question = get_object_or_404(Question,pk=question_id) #id값을 얻어와서 question에 넣음 / 값없을시 404에러
    context = {'question':question}
    return render(request,'pybo/question_detail.html',context) #detail html에 저장된 context를 보냄

def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question_id)

