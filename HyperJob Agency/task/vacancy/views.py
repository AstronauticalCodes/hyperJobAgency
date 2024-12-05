from django.shortcuts import render
from django.views import View
from .models import Vacancy
# Create your views here.


class VacancyView(View):
    template_name = 'vacancy/vacancies.html'
    model = Vacancy

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'vacancies': self.model.objects.all()})