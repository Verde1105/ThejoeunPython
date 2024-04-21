from django.urls import path
from .views import base_views, question_views, answer_views, comment_views, vote_views


app_name = 'pybo'#url관리하는 너를 pybo라는 이름으로 부를꺼야.


urlpatterns = [
    #질문 추천에 있는것들
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote_answer'),


    #베이스에 있는것들
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),#네임은 url에 이름지어준것, html에서 이름 부르면 얘로 연결됨, 얘한테 필요한 값(id)필수
    
    #퀘스천에 있는것들
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),

    #답변에 있는것들
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),
    
    #댓글에 있는것들
    path('comment/create/question/<int:question_id>/', comment_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', comment_views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_delete_question, name='comment_delete_question'),

    #comment_views(대댓글기능)
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),

]