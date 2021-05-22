from django.urls import path,include
# from django.contrib.auth import views as auth_views


from quiz import views

urlpatterns = [
    path('',views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('home/<int:level_id>',views.home, name='home'),
    path('get/<int:level_id>/', views.get_mcq, name='get_mcq'),
    path('post/<int:level_id>/<int:question_id>/', views.validate_mcq, name='validate_mcq'),
    path('score/<int:level_id>', views.score, name='score'),
    path('quiz_again/<int:level_id>', views.quiz_again, name='quiz_again'),
]