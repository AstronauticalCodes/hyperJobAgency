from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView

urlpatterns = [
    path('resumes/', views.ResumeView.as_view()),
    path('', views.index),
    path('login', views.HyperJobLoginView.as_view()),
    path('signup', views.HyperJobSignUpView.as_view()),
    path('logout/', views.LogOut),
   # path('logout/', RedirectView.as_view(url='/login')),
]
