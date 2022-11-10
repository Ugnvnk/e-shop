
from allauth.account.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordResetConfirmView
from django.views import View
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import FormView, ListView

from .forms import UserCreationForm, MySetPasswordForm, ProductInput
from .models import Category


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

from django.shortcuts import render


def main(request):
    cats = Category.objects.filter(parent=None)

    context = {'cats': cats, 'cat_selected': 0}

    return render(request, "main/main.html", context = context )


class ShowCategory(ListView):


    model = Category
    template_name = "main/show_category.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['cat'] = Category.objects.get(slug=self.kwargs['cat_slug'])
        context['cats'] = Category.objects.filter(parent=None)
        context['cat_selected'] = context['cat'].pk
        context['children'] = context['cat'].category_set.all()




        return context


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProductInput(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProductInput()

    return render(request, 'main/product_form.html', {'form': form})




