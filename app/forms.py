from django import forms
from django.core import validators
class Student(forms.Form):
    student_name=forms.CharField(max_length=100)
    student_age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    url=forms.URLField()
    mobile_number=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
