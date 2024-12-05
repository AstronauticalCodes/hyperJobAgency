from django.urls import path
from . import views

urlpatterns = [
    path('resumes/', views.ResumeView.as_view()),
    path('', views.index),
    path('login', views.HyperJobLoginView.as_view()),
]
