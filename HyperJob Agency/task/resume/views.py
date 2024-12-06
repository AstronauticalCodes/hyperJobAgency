from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.views import View
from . models import Resume
from .forms import ResumeForm
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')

class ResumeView(View):
    template_name = 'resume/resumes.html'
    model = Resume

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'resumes': Resume.objects.all()})


class ResumeCreateView(View):
    template_name = 'resume/resume_create.html'
    model = Resume
    form = ResumeForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, self.template_name, context={'form': self.form})
        else:
            return HttpResponse("<h3>Login First!!</h3>")

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        # print(request.POST['description'])
        usernames = [user.username for user in User.objects.all()]
        # print(usernames)
        custom_POST = request.POST.copy()
        custom_POST['author'] = str(usernames.index(request.user.username) + 1)
        # print('request', request.POST)
        # print('custom', custom_POST)
        form = self.form(custom_POST)
        # print(request.user.username)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data['description'])
            return redirect('/')
        else:
            return HttpResponse("<h2>Not valid</h2>")
