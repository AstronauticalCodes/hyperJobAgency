from django.shortcuts import render, redirect
from django.views import View
from . models import Resume
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .models import SignUpForm
from django.contrib.auth import logout


def index(request):
    return render(request, 'index.html')

class ResumeView(View):
    template_name = 'resume/resumes.html'
    model = Resume

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'resumes': Resume.objects.all()})


class HyperJobLoginView(LoginView):
    form = AuthenticationForm
    # redirect_authenticated_user = True
    template_name = 'login.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'form': self.form})


class HyperJobSignUpView(CreateView):
    form = UserCreationForm
    template_name = 'signup.html'
    success_url = 'login'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'form': self.form})


    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/login')
        else:
            print('not valid')
            return HttpResponse("<h2>not vaild</h2>")


def LogOut(request):
    logout(request)
    return redirect('/')