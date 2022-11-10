from django.urls import path, include
from django.views.generic import TemplateView

from . import views
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('accounts/cabinet/', TemplateView.as_view(template_name='main/cabinet.html'), name='cabinet'),
    path("accounts/reset/<uidb64>/<token>/", views.MyPasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', Register.as_view(), name='register'),
    path('login_modal/', MyLoginView.as_view(), name='login_modal'),
    path('product_input/', get_name, name='productInput'),
    path('accounts/', include('allauth.urls')),
    path('category/<slug:cat_slug>/', ShowCategory.as_view(), name='category'),
]



