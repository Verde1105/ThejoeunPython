from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length = 200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True,blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question') #오, 이거 부트할때 본것같은데? 

    def __str__(self):
        return self.subject#서브젝 = 제목. 얘가 있어야. 등록된 id가 아닌 제목을 표시해준다.


class Answer(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True,blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer') #부트에서 봤던 JPA형식이랑 비슷하다.

class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True,blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete = models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete = models.CASCADE)




