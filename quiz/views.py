from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic.edit import View

from quiz.models import *
from quiz.tasks import count


class HomeView(View):
    def get(self, request, *args, **kwargs):
        qid = Question.objects.first().id
        return redirect("/question/" + str(qid))


class QuestionView(View):
    template_name = 'quiz/question.html'

    def get(self, request, question_id):
        question = Question.objects.get(id=question_id)
        choices = Choice.objects.filter(ques=question)
        context = {'question': question, 'choices': choices}
        return render(request, self.template_name, context)

    def post(self, request, question_id):
        question = Question.objects.filter(id__gt=question_id).first()
        count.delay()
        if question:
            return redirect("/question/" + str(question.id))
        else:
            context = {'score': 0}
            return render(request, "quiz/complete.html", context)
