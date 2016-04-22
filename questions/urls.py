from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', QuestionList.as_view(), name="question_list"),
    url(r'^(?P<pk>\d+)/$', QuestionDetail.as_view(), name="question_view"),
    url(r'^create/$', QuestionCreate.as_view(), name="question_create"),
    url(r'^(?P<pk>\d+)/update/$', QuestionUpdate.as_view(), name="question_update"),
    url(r'^(?P<pk>\d+)/ajax.js/$', QuestionCommentAjax.as_view(), name="question_ajax"),
    url(r'^(?P<pk>\d+)/likes_ajax.js/$', QuestionLikesAjax.as_view(), name="likes_ajax"),

]
