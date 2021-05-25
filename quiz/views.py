from django.shortcuts import redirect, render
from django.views.generic.edit import View

from quiz.models import *
from quiz.tasks import calculate_score


class HomeView(View):
    def get(self, request, *args, **kwargs):
        current_user = request.user
        Test.objects.create(user=current_user, active=True)
        question = Question.objects.first()
        return redirect("/question/" + str(question.id))


class QuestionView(View):
    template_name = 'quiz/question.html'

    def get(self, request, question_id):
        question = Question.objects.get(id=question_id)
        choices = Choice.objects.filter(ques=question)
        context = {'question': question, 'choices': choices}
        return render(request, self.template_name, context)

    def post(self, request, question_id):
        current_test = Test.objects.filter(active=True).last()
        question = Question.objects.get(id=question_id)
        next_question = Question.objects.filter(id__gt=question_id).first()
        if next_question:
            choice_id = int(request.POST.get('choice'))
            selected_option = Choice.objects.get(id=choice_id)
            TestResponses.objects.create(
                test=current_test, question=question, choice=selected_option)
            return redirect("/question/" + str(next_question.id))
        else:
            calculate_score.delay(current_test.id)
            context = {}
            return render(request, "quiz/complete.html", context)


class TestsDashboardView(View):
    template_name = 'quiz/dashboard.html'

    def get(self, request):
        # tests = Test.objects.all()
        tests = Test.objects.select_related('user').all()
        context = {'tests': tests}
        return render(request, self.template_name, context)

