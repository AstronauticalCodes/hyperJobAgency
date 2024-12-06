from django.shortcuts import render, redirect
from django.views import View
from .models import Vacancy
from django.http import HttpResponse
from .forms import VacancyForm
from django.contrib.auth.models import User
# Create your views here.


class VacancyView(View):
    template_name = 'vacancy/vacancies.html'
    model = Vacancy

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'vacancies': self.model.objects.all()})


class VacancyCreateView(View):
    template_name = "vacancy/vacancy_create.html"
    form = VacancyForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return render(request, self.template_name)
            else:
                return HttpResponse('<h3>This page can only be accessed by Manager!</h3>')
        else:
            return HttpResponse('<h2>Login First!!</h2>')

    def post(self, request, *args, **kwargs):
        usernames = [user.username for user in User.objects.all()]
        custom_POST = request.POST.copy()
        custom_POST['author'] = str(usernames.index(request.user.username) + 1)
        form = self.form(custom_POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return HttpResponse("<h2>Not valid</h2>")