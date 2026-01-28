from django import forms
from .models import *


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'