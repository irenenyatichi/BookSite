from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Record

class BookRegistrationForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"

    def __str__(self):
        return self.field_name