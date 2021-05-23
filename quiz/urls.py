from django.urls import path, include
from django.contrib.auth.decorators import login_required

from quiz import views

urlpatterns = [
    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login_request, name='login'),
    # path('logout/', views.logout_request, name='logout'),
    path('', login_required(views.HomeView.as_view()), name='home'),
]
