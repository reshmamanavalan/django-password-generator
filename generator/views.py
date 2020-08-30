from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')
def password(request):
    characters=list('abcdefghijklmnopqrstuvwxyz')
    if(request.GET.get('Uppercase')):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if(request.GET.get('specialchar')):
        characters.extend(list('!@#$%^&*()'))
    if(request.GET.get('numbers')):
        characters.extend(list('1234567890'))
    length=int(request.GET.get('length'))
    thepassword=''
    for x in range(length):
        thepassword+=random.choice(characters)
    return render(request,'generator/password.html',{'password':thepassword})
def fp(request):
    return render(request,'generator/fp.html')
def Length(request):
    return render(request,'generator/Length.html')
def numbers(request):
    return render(request,'generator/numbers.html')
def specialchar(request):
    return render(request,'generator/specialchar.html')
def uppercase(request):
    return render(request,'generator/uppercase.html')
