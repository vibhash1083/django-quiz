from django.urls import path, include
from django.contrib.auth.decorators import login_required

from quiz import views

urlpatterns = [
    path('', login_required(views.HomeView.as_view()), name='home'),
    path('question/<question_id>', login_required(views.QuestionView.as_view()), name='question'),
    path('dashboard', login_required(views.TestsDashboardView.as_view()), name='dashboard'),
]
