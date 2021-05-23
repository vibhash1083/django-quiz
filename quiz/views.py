import random

from core import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.edit import View

from quiz.models import *


class HomeView(View):
    template_name = 'quiz/home.html'
    
    def get(self, request, *args, **kwargs):
        questions_list = []
        questions = Question.objects.all()
        for question in questions:
            choices = Choice.objects.filter(ques = question)
            questions_list.append({'question': question, 'choices': choices})
        context = {'data': questions_list}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        questions_list = []
        questions = Question.objects.all()
        for question in questions:
            choices = Choice.objects.filter(ques = question)
            questions_list.append({'question': question, 'choices': choices})
        context = {'data': questions_list}
        return render(request, self.template_name, context)
