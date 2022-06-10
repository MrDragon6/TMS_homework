from django.http import HttpResponseBadRequest, HttpRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login

from .models import Reader


@csrf_exempt
def home(request):
    return render(request, 'main/home.html')


@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html')

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            django_login(request, user)
            return render(request, 'auth/profile.html', context={'username': user.get_username()})
        else:
            return render(request, 'auth/login.html')

    return HttpResponseBadRequest('Error')


@csrf_exempt
def signup(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'auth/signup.html')

    elif request.method == 'POST':
        data = request.POST.dict()
        data.pop('csrfmiddlewaretoken')
        password = data.pop('password')

        user: User = User.objects.create(**data)
        user.set_password(password)
        user.save()

        Reader.objects.create(user=user)

        reader = Reader(user=user)
        reader.save()

        return render(request, 'auth/login.html')

    return HttpResponseBadRequest('Error')
