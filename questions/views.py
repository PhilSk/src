# coding: utf-8
from django.shortcuts import resolve_url, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from comments.models import Comment
from .models import Question
from .forms import QuestionListForm
from django.db.models import Q
from django.db.models import Count
from django.http import JsonResponse


class QuestionCreate(CreateView):

    model = Question
    template_name = "questions/create.html"
    fields = ('title', 'text', 'topics', 'is_published')

    def get_success_url(self):
        return resolve_url('questions:question_view', pk=self.object.pk)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(QuestionCreate, self).form_valid(form)


class QuestionUpdate(UpdateView):

    model = Question
    template_name = "questions/update.html"
    fields = ('title', 'text', 'is_published')

    def get_success_url(self):
        return resolve_url('questions:question_view', pk=self.object.pk)


class QuestionList(ListView):

    model = Question
    template_name = "questions/question_list.html"
    context_object_name = 'questions'

    def dispatch(self, request, *args, **kwargs):
        self.form = QuestionListForm(request.GET)
        self.form.is_valid()
        self.search = self.form.cleaned_data.get('search')
        self.sort_field = self.form.cleaned_data.get('sort_field')
        return super(QuestionList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(QuestionList, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def get_queryset(self):
        queryset = super(QuestionList, self).get_queryset()
        if self.request.user.is_authenticated():
            queryset = queryset.filter(Q(author=self.request.user) | Q(is_published=True))
        else:
            queryset = queryset.filter(is_published=True)
        if self.search:
            queryset = queryset.filter(Q(title__icontains=self.search) | Q(text__icontains=self.search))
        if self.sort_field:
            queryset = queryset.order_by(self.sort_field)
        queryset = queryset.annotate(comments_count=Count('comments__id'))
        return queryset


class QuestionCommentAjax(DetailView):

    template_name = 'questions/question_comment_ajax.html'
    model = Question
    context_object_name = 'question'


class QuestionLikesAjax(DetailView):

    template_name = 'questions/question_likes_ajax.html'
    model = Question
    context_object_name = 'question'


class QuestionDetail(CreateView):
    model = Comment
    template_name = 'questions/question_detail.html'
    fields = ('text', )

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.question = get_object_or_404(Question, id=pk)
        return super(QuestionDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(QuestionDetail, self).get_context_data(**kwargs)
        context['question'] = self.question
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.question = self.question
        return super(QuestionDetail, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('questions:question_view', pk=self.question.pk)

