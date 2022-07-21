from django.urls import path
from . import views


app_name = 'pybo'

urlpatterns =[
    path('',views.index, name='index'), #name값은 프로그램수정시의 번거로움을 제거하기위함
    path('<int:question_id>/',views.detail, name='detail'), #db테이블 id / 내용 매핑
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),

]

