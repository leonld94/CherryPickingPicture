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
    if request.COOKIES.get('username') is not None:
        username = request.COOKIES.get('username')
        password = request.COOKIES.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("../")
        else:
            return render(request, "account/login.html")
    elif request.method == "POST":
        un = request.POST['id'];
        passwd = request.POST['password'];
        user = auth.authenticate(request, username=un, password = passwd);
        if user is not None:
            auth.login(request, user)
            if request.POST.get("keep_login") == "TRUE":
                response = render(request, 'Main_page.html')
                response.set_cookie('username', un)
                response.set_cookie('password', passwd)
                return response
            return redirect('../');
    return render(request, 'Login.html');


def signup(request):
    if request.method == "POST":
        if User.objects.filter(username = request.POST['id']).exists():
            context = {'failure' : "이미 존재하는 아이디입니다."}
            return render(request ,'Signup.html', context);
        elif request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['id'], password=request.POST['password1'], first_name=request.POST['nickname']
            )
            #return render(request, 'Login.html');
            return redirect('../Login');
        elif request.POST['password1'] != request.POST['password2']:
            context = {'failure' : "비밀번호가 일치하지 않습니다."}
            return render(request, 'Signup.html', context);
    return render(request, 'Signup.html');