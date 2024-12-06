from django.urls import path
from . import views

urlpatterns = [
    path('', views.VacancyView.as_view()),
    path('new/', views.VacancyCreateView.as_view()),
]
