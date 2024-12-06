from .models import Resume
from django.forms import ModelForm


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['description', 'author']