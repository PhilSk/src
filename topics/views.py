from django.views.generic import ListView
from .models import Topic


class TopicList(ListView):

    model = Topic
    template_name = "topics/topic_list.html"
    context_object_name = 'topic'





