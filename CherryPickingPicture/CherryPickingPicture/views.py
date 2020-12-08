from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def main(request):
    template = loader.get_template('Main_page.html');
    return HttpResponse(template.render());


def login(request):
    template = loader.get_template('Login.html');
    return HttpResponse(template.render());