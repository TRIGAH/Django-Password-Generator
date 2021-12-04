from django.shortcuts import render
import random


# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    lenght = int(request.GET.get('length'))
    password = ''
    for x in range(lenght):
        password += random.choice(characters)

        if(request.GET.get('uppercase')):
            characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        if (request.GET.get('numbers')):
            characters.extend(list('1234567890'))
        if(request.GET.get('special')):
            characters.extend(list('!@#$%^&*()_+'))               
    return render(request,'generator/password.html',{'password':password})    
