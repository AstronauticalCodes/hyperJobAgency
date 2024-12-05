from django.shortcuts import render
from django.views import View
from . models import Resume


class ResumeView(View):
    template_name = 'resumes/resumes.html'
    model = Resume

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={'resumes': Resume.objects.all()})