from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def main(request):
    template = loader.get_template('Main_page.html');
    return HttpResponse(template.render());


def login(request):
    if request.method == "POST":
        un = request.POST['id'];
        passwd = request.POST['password'];
        user = auth.authenticate(request, username=un, password = passwd);
        if user is not None:
            auth.login(request, user)
            return redirect('');
    return render(request, 'Login.html');


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['id'], password=request.POST['password1'], first_name=request.POST['nickname']
            )
            return render(request, 'Login.html');
            #return redirect('login');
    return render(request, 'Signup.html');