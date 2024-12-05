from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from resume.models import SignUpForm
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return HttpResponse('''<h2>Welcome to HyperJob!</h2>
<p><a href="/login">Login</a></p>
<p><a href="/logout">Logout</a></p>
<p></p><a href="/signup">Signup</a></p>
<p><a href="/vacancies">Vacancies</a></p>
<p><a href="/resumes">Resumes</a></p>
<p><a href="/home">Personal Profile</a></p>''')


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

