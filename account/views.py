from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login

from account.models import Investor


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.add_message(request, messages.WARNING, 'Произошла ошибка.Проверьте данные')
            return redirect('login')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
        front_passport = request.FILES.get('front_passport')
        back_passport = request.FILES.get('back_passport')
        selfie_passport = request.FILES.get('selfie_passport')

        print(front_passport, back_passport, selfie_passport)

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')
        if password_1 == password_2:
            user = User.objects.create(first_name=first_name, email=email, last_name=last_name, username=username)
            user.set_password(password_1)
            user.save()
            investor = Investor.objects.create(user=user, phone=phone, front_passport=front_passport,
                                               back_passport=back_passport,
                                               selfie_passport=selfie_passport)
            investor.save()
            return redirect('login')
        else:
            messages.add_message(request, messages.WARNING, 'Произошла ошибка.Проверьте данные')
            return redirect('register')
    return render(request, 'register.html')


def dashboard(request):
    return render(request, 'dashboard.html')
