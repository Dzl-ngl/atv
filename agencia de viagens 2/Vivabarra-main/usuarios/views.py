from django.shortcuts import render

def home(req): 
    return render(req, 'index.html')

def turis(req):
    return render(req, 'turismo.html')

def hoteis(req):
    return render(req, 'hoteis.html')

def rest(req):
    return render(req, 'restaurante.html')

# Create your views here.
