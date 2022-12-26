from django.shortcuts import render
from django .http import HttpResponse

# Create your views here.
def tirupathi(request):
    return HttpResponse('<h1><marquee>nature of god</marquee></h1>')
def bangalore(request):
    return HttpResponse('<h2>It is a silicon city</h2>')