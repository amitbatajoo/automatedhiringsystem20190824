'''
Created on Aug 25, 2019

@author: amitbatajoo
'''
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')