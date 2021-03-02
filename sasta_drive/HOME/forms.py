from django.contrib.auth import models
from .models import Through, FileObject
from django.contrib.auth.models import User
from django import forms

class FileForm(forms.ModelForm):
    class Meta:
        model = FileObject
        fields = ['Name', 'File']