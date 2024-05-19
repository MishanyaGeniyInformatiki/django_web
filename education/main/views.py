import time

from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions
from .forms import QuestionForm, QuestionForm2


# Create your views here.

from django.views.generic import TemplateView


class MultiFormView(TemplateView):
    template_name = 'multi_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_profile_form'] = QuestionForm()
        context['avatar_upload_form'] = QuestionForm2()
        return context


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'aa', 'fff']
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def questions(request):
    data = Questions.objects.all()
    questions_num = len(data)
    correct_input = [True]*questions_num
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # print(form.cleaned_data['question_id'])
            try:
                a = float(form.cleaned_data['answer'])
            except ValueError:
                # for i in range(questions_num):
                correct_input[0] = False

            if False not in correct_input:
                if form.cleaned_data is not None:
                    Questions.objects.filter(id=form.cleaned_data['question_id']).update(user_answer=float(form.cleaned_data['answer']))
                else:
                    for i in data:
                        Questions.objects.filter(id=i.id).update(user_answer=None)
    else:
        for i in data:
            Questions.objects.filter(id=i.id).update(user_answer=None)
    # time.sleep(4)
    data_forms = [{'correct_input': correct_input, 'question_id': data[i].id, 'name': data[i].name, 'question_text': data[i].question_text, 'correct_answer': data[i].correct_answer, 'user_answer': data[i].user_answer, 'form': QuestionForm()} for i in range(questions_num)]
    # print(data_forms)
    return render(request, 'main/questions.html', {'data_forms': data_forms})
                  # {'form1': form, 'form2': form2, 'data': data})

def lesson(request):
    return render(request, 'main/lesson.html')