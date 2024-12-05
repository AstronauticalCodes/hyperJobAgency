from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.views import View
from . models import Resume


def index(request):
    return render(request, 'index.html')

class ResumeView(View):
    template_name = 'resume/resumes.html'
    model = Resume

    def get(self, request, *args, **kwargs):
        # if request.user.is_staff:
        #     return HttpResponse("<h2>Manager</h2>")
        # return HttpResponse("<h2>Candidate</h2>")
        return render(request, self.template_name, context={'resumes': Resume.objects.all()})
