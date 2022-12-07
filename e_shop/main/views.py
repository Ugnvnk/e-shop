from allauth.account.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordResetConfirmView
from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import UserCreationForm, MySetPasswordForm


class MyLoginView(View):

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return JsonResponse(data={'status': 201}, status=200)
            return JsonResponse(data={'status': 400, 'error': 'Логин и пароль не валидные'}, status=200)
        return JsonResponse(data={'status': 400, 'error': 'Введите логин и пароль'}, status=200)


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = MySetPasswordForm


class Register(View):
    """
    template_name = 'main/registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)
    """
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            return JsonResponse(data={'status': 201}, status=200)
        return JsonResponse(data={'status': 400, 'error': 'Логин и пароль не валидные'}, status=200)


class SocialLoginView(LoginView):
    pass
