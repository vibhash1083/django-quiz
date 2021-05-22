from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
import random
from core import settings
from quiz.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url=settings.LOGIN_URL)
def index(request):
    lvl = Level.objects.get(user=request.user)
    return redirect('home', level_id=lvl.id)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'quiz/signup.html', {'form': form})



def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                lvl = Level.objects.get_or_create(user=user,level_flag=1)
                return redirect(settings.LOGIN_REDIRECT_URL,level_id=lvl[0].id)
                # return render(request,'quiz/home.html',{'level':lvl[0]})
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request,'quiz/login.html', {'form': form})

@login_required(login_url=settings.LOGIN_URL)
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    q = Questions.objects.filter(is_repeated=True).update(is_repeated=False,is_correct=False)
    l = Level.objects.all().update(level_flag=1,score=0)
    return redirect('login')

@login_required(login_url=settings.LOGIN_URL)
def home(request,level_id):
    level = Level.objects.get(id=level_id)
    return render(request,'quiz/home.html',{'level':level})

@login_required(login_url=settings.LOGIN_URL)
def validate_mcq(request,level_id,question_id=None):
    score_update = Level.objects.get(id=level_id)
    get_question = Questions.objects.get(id = question_id)
    get_answer = Answers.objects.filter(ques=get_question)
    user_response = request.POST.get("answer")
    if random.choice(get_answer).right_answer == user_response:
        get_question.is_repeated = True
        get_question.is_correct = True
        get_question.save()
        if score_update.level_flag == 0:
            score_update.level_flag = 1
        elif score_update.level_flag >= 5:
            score_update.level_flag = 5
        else:
            score_update.level_flag = score_update.level_flag+1
        score_update.save()
        if score_update.score >= 0:
            score_update.score = score_update.prev_score = score_update.score+score_update.level_flag
        score_update.save()
        return redirect('get_mcq', level_id=score_update.id)
    else:
        get_question.is_repeated = True
        get_question.save()
        if score_update.score > 0:
            score_update.score = score_update.score-1
        score_update.level_flag = score_update.level_flag-1
        # level_info = score_update.track_score_and_level(get_question.is_correct)
        if score_update.level_flag == 0:
            score_update.level_flag = 1
        if score_update.level_flag >= 5:
            score_update.level_flag = 5
        
        score_update.save()
        return redirect('get_mcq', level_id=score_update.id)

    return True

@login_required(login_url=settings.LOGIN_URL)
def get_mcq(request,level_id):
    score_info = Level.objects.get(id=level_id)
    if Questions.objects.filter(is_repeated=True).count() > 10:
        return render(request, 'quiz/scorecard.html', {'score_info':score_info})
    else:
        question = random.choice(Questions.objects.filter(level_no=score_info.level_flag, is_repeated=False))
        options = Answers.objects.filter(ques=question)
        ques_left = 10 - Questions.objects.filter(is_repeated=True).count()
        return render(request, 'quiz/quiz.html', {'data': options,'ques':question, 'sco':score_info,'ques_left':ques_left})

@login_required(login_url=settings.LOGIN_URL)
def score(request,level_id):
    score_info = Level.objects.get(id=level_id)
    return render(request, 'quiz/scorecard.html', {'score_info':score_info})

@login_required(login_url=settings.LOGIN_URL)
def quiz_again(request,level_id):
    q = Questions.objects.filter(is_repeated=True).update(is_repeated=False,is_correct=False)
    l = Level.objects.all().update(level_flag=1,score=0)
    return redirect('get_mcq', level_id=level_id)