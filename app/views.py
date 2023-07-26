from django.shortcuts import render
from django.http import HttpResponse
from app import forms

# Create your views here.

def student_form(request):
    SO=Student()
    d={'SO':SO}
    if request.method=='POST':
        SFD=Student(request.POST)
        if SFD.is_valid():
            return HttpResponse('IS _ VALID')
        else:
            return HttpResponse('is not valid')
        
    return render (request,'student_form.html',d)
