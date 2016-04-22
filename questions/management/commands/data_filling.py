from django.core.management import BaseCommand
from django.contrib.auth.models import User
from comments.models import Comment
from questions.models import Question
from topics.models import Topic
import random
import datetime


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = list(User.objects.all())

        for i in range(10):
            t = Topic()
            t.name = u'Topic Name {}'.format(i)
            t.description = u'Topic Description {}'.format(i)
            t.save()
        topics = list(Topic.objects.all())

        for j in range(100):
            q = Question()
            q.author = random.choice(users)
            q.title = u'title {}'.format(j)
            q.text = u'text {}'.format(j)
            q.pub_date = datetime.datetime.now()
            q.is_published = True
            q.save()
            q.topics = random.sample(topics, random.randint(1, 6))
        questions = list(Question.objects.all())

        for k in range(100):
            c = Comment()
            c.author = random.choice(users)
            c.question = random.choice(questions)
            c.text = u'text {}'.format(k)
            c.pub_date = datetime.datetime.now()
            c.save()


