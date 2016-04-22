from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', TopicList.as_view(), name="topic_list"),
]
