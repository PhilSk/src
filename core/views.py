from django.views.generic import TemplateView
from questions.models import Question
from comments.models import Comment



class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['last_questions'] = Question.objects.filter(is_published=True)[:5]
        context['last_answers'] = Comment.objects.filter(question__is_published=True)[:5]
        return context
