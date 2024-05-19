import uuid

from django.db import models


class Questions(models.Model):
    name = models.TextField(blank=True)
    question_text = models.TextField(blank=True)
    correct_answer = models.FloatField()
    user_answer = models.FloatField(blank=True, default=None, null=True)


# Questions(name='Тест 1', question_text='Введи 1', correct_answer=1.0).save()
# Questions(name='Тест 2', question_text='Введи 2', correct_answer=2, user_answer=None).save()