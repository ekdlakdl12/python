from django.db import models

# Create your models here.

class Question(models.Model): #models.model 이게 뭔지 아직모름
    subject = models.CharField(max_length=200,default='') #char값 크기 크기제한o
    content = models.TextField() #텍스트 영역 크기제한x
    create_date = models.DateTimeField() #dateTime
    def __str__(self): #id가 아닌 제목을 표시해줌
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE) #외래키 삭제시 답변테이블도 같이 삭제
    content = models.TextField()
    create_date = models.DateTimeField() #dateTime

