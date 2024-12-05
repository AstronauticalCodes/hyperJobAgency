from django.shortcuts import render
from django.views import View
from . models import Resume
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse


def index(request):
    return HttpResponse('''<h2>Welcome to HyperJob!</h2>
<p><a href="/login">Login</a></p>
<p><a href="/logout">Logout</a></p>
<p></p><a href="/signup">Signup</a></p>
<p><a href="/vacancies">Vacancies</a></p>
<p><a href="/resumes">Resumes</a></p>
<p><a href="/home">Personal Profile</a></p>''')


class ResumeView(View):
    template_name = 'resume/resumes.html'
    model = Resume

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'resumes': Resume.objects.all()})


class HyperJobLoginView(LoginView):
    form = AuthenticationForm
    # redirect_authenticated_user = True
    template_name = 'login.html'
    success_url = 'login'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'form': self.form})


class HyperJobSignUpView(CreateView):
    form = UserCreationForm
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'form': self.form})