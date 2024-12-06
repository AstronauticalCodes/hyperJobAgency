from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.ResumeView.as_view()),
    path('new/', views.ResumeCreateView.as_view())
    # path('', views.index),
   # path('logout/', RedirectView.as_view(url='/login')),
]
