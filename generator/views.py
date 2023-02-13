from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')


def password(request):
    
    length = int(request.GET.get('length'))
    # uppercase = bool(request.GET.get('uppercase'))
    # numbers = bool(request.GET.get('numbers'))
    # symbols = bool(request.GET.get('symbols'))

    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    alphabet_up = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    num_list = list('1234567890')
    symbol_list = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

    char_list = alphabet * 3

    char_list += alphabet_up if request.GET.get('uppercase') else char_list
    char_list += num_list if request.GET.get('numbers') else char_list
    char_list += symbol_list if request.GET.get('symbols') else char_list

    the_password = ''

    for i in range(length):
        the_password += random.choice(char_list)

    return render(request, 'generator/password.html', {'password': the_password})

