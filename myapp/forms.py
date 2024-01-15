from django import forms
from .models import blog
class Postform(forms.ModelForm):
  class Meta:
   model = blog
   fields = ['title','dis']