from django.contrib import admin
from .models import Question


# Register your models here.
# admin.site.register(Question)

class QuestionAdmin(admin.ModelAdmin):#검색기능
    search_fields = ['subject']#제목으로 찾기

admin.site.register(Question, QuestionAdmin)