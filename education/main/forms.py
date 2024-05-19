from .models import Questions
from django.forms import ModelForm, TextInput, Form, CharField, IntegerField


class QuestionForm(Form):
    # def __init__(self, *args, **kwargs):
    #     self.correct_answer = kwargs.pop('correct_answer')
    #     super(QuestionForm, self).__init__(*args, **kwargs)

    answer = CharField(max_length=255)
    # whatafuck = CharField(max_length=255)
    correct_answer = CharField(max_length=255)
    question_id = IntegerField()


class QuestionForm2(Form):
    # def __init__(self, *args, **kwargs):
    #     self.correct_answer = kwargs.pop('correct_answer')
    #     super(QuestionForm, self).__init__(*args, **kwargs)

    answer = CharField(max_length=255)
    # correct_answer = CharField(max_length=255)
