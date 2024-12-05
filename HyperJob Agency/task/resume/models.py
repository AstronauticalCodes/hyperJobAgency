from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class Resume(models.Model):
    description = models.TextField(max_length=1024)
    author = models.ForeignKey(User, on_delete=models.PROTECT)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']