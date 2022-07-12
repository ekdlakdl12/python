from django.contrib import admin
from.models import Question #Question 모델 추가
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question,QuestionAdmin) #키워드 검색 부분

