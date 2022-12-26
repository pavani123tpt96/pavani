from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def gayathri(request):
    return HttpResponse('<b>she is a dancer</b>')
def deepu(request):
    return HttpResponse('<i>deepu is the correct person to gayathri </i>')