# coding: utf-8
from django import forms


class QuestionListForm(forms.Form):

    search = forms.CharField(required=False, initial='Поиск')
    sort_field = forms.ChoiceField(choices=(('id', 'ID'), ('pub_date', u'Дата создания'), ('is_published', u'Неопубликованные')), required=False, initial=id)
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(QuestionListForm, self).form_valid(form)


class QuestionForm(forms.Form):

    title = forms.CharField(max_length=255 )
    text = forms.CharField()
