from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from account.models import User
from userpanel.forms import ChangePasswordForm, EditProfileModelForm


@login_required
def user_panel_menu_component(request: HttpRequest):
    return render(request, 'userpanel/components/components.html')


@login_required
def user_dashboard(request: HttpRequest):
    return render(request, 'userpanel/dashboard.html')


@method_decorator(login_required, name='dispatch')
class ChangePassword(View):

    def get(self, request):
        form = ChangePasswordForm()
        return render(request, 'userpanel/change_password.html', context={
            'form': form
        })

    def post(self, request: HttpRequest):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_password = request.POST.get('current_password')
            new_password = request.POST.get('new_password')
            repeat_password = request.POST.get('repeat_password')
            user_id = request.user.id
            user_data = User.objects.filter(id=user_id).first()
            if user_data.check_password(current_password):
                if new_password == repeat_password:
                    user_data.set_password(new_password)
                    user_data.save()
                    logout(request)
                    return redirect(reverse("login-page"))
                else:
                    raise ValidationError("رمزعبور و تکرار ان با هم مغایرت دارد.")

            form.add_error('current_password', 'رمز عبور وارد شده اشتباه است.')

        return render(request, 'userpanel/change_password.html', context={
            'form': form
        })


@method_decorator(login_required, name='dispatch')
class EditProfile(View):
    def get(self, request: HttpRequest):
        form = EditProfileModelForm(instance=request.user)
        return render(request, 'userpanel/edit_profile.html', context={
            'form': form
        })

    def post(self, request: HttpRequest):
        form = EditProfileModelForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('dashboard-page'))
        return render(request, 'userpanel/edit_profile.html', context={
            'form': form
        })


