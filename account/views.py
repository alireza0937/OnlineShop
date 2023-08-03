from django.contrib.auth import login, logout
from django.core.exceptions import ValidationError
from django.http import HttpRequest, Http404, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from account.forms import RegisterForm, LoginForm, ForgotPasswordForm, ChangePasswordForm
from account.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class RegisterView(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/register.html', context={
            'form': form
        })

    def post(self, request: HttpRequest):
        message = False
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get("password")
            user_exists: bool = User.objects.filter(email__iexact=email).exists()
            if user_exists:
                register_form.add_error('email', 'ایمیل تکراری است')
            else:
                new_user = User(email=email,
                                is_active=False,
                                email_activation_code=get_random_string(12),
                                username=email)
                new_user.set_password(password)
                new_user.save()
                message = True
                return render(request, 'account/register.html', context={
                    'msg': message
                })

        register_form = RegisterForm()
        return render(request, 'account/register.html', context={
            'form': register_form,
            'msg': message
        })


def authentication(request, activation_code):
    user = User.objects.filter(email_activation_code=activation_code).first()
    if user is not None:
        user.is_active = True
        user.save()
        return redirect(reverse('index-page'))
    else:
        raise Http404


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'account/login.html', context={
            'form': login_form
        })

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            user = User.objects.filter(email__iexact=email).first()
            if user is not None:
                if user.check_password(password) and user.is_active:
                    login(request, user)
                    return redirect(reverse('index-page'))
                else:
                    login_form.add_error('password', 'Wrong Password or Email')
            else:
                login_form.add_error('email', 'Wrong Password or Email')

        return render(request, 'account/login.html', context={
            'form': login_form
        })


def logout_account(request: HttpRequest):
    logout(request)
    return redirect(reverse('index-page'))


@method_decorator(login_required, name='dispatch')
class ForgotPassword(View):
    def get(self, request: HttpRequest):
        form = ForgotPasswordForm()
        return render(request, 'account/Forgot_Password.html', context={
            'form': form
        })

    def post(self, request: HttpRequest):
        email_is_correct = False
        entered_email = request.POST.get('email')
        user_exist = User.objects.filter(email__iexact=entered_email).first()
        if user_exist is not None:
            email_is_correct = True
        else:
            email_is_correct = False

        return render(request, 'account/Forgot_Password.html', context={
            'msg': email_is_correct
        })


@method_decorator(login_required, name='dispatch')
class ChangePassword(View):
    def get(self, request: HttpRequest, link):
        sent_link = User.objects.filter(email_activation_code=link).first()
        if sent_link is not None:
            form = ChangePasswordForm()
            return render(request, 'account/Change_Password.html', context={
                'form': form,
                'user_link': link
            })
        else:
            return HttpResponse("link is not valid")

    def post(self, request: HttpRequest, link):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = request.POST.get('new_password')
            repeat_password = request.POST.get('repeat_new_password')
            if new_password == repeat_password:
                current_user = User.objects.filter(email_activation_code__iexact=link).first()
                current_user.set_password(new_password)
                current_user.email_activation_code = get_random_string(12)
                current_user.save()
                return redirect(reverse('login-page'))
            raise ValidationError("رمز عبور وارد شده با تکرار منطبق نیست")

        return render(request, 'account/Change_Password.html', context={
            'form': form
        })
