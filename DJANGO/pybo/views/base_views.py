from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from ..models import Question
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count

def index(request):
    """
    pybo 목록 출력
    """

    #입력인자
    page = request.GET.get('page','1') #페이지
    kw = request.GET.get('kw','') #검색어
    so = request.GET.get('so','recent') #정렬기준
    
    #정렬
    if so == 'recommend':
       question_list = Question.objects.annotate(
        num_voter=Count('voter')). order_by('-num_voter','-create_date')
    elif so == 'popular':
       question_list = Question.objects.annotate(
        num_answer=Count('answer')). order_by('-num_naswer', '-create_date')
    else: #recent
        question_list = Question.objects.order_by('-create_date')


    #조회
    #question_list = Question.objects.order_by('-create_date')#order_by조회한 데이터를 특정 속성으로 정렬//create_date의 앞에 - 를 붙이면 역순을 의미한다.
    if kw:
      question_list = question_list.filter(
        Q(subject__icontains=kw) | #제목검색
        Q(content__icontains=kw) | #내용 검색
        Q(author__username__icontains=kw) | #질문 글쓴이 검색
        Q(answer__author__username__icontains=kw) # 답변 글쓴이 검색
      ).dustinct()

    
    #페이징 처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    
    context = {'question_list': page_obj, 'page':page, 'kw':kw}
    #return HttpResponse("pybo에 오신것을 환영합니다.")
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    #question = Question.objects.get(id = question_id)
    question = get_object_or_404(Question, pk = question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)







