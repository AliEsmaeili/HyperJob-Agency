from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.views.generic.base import TemplateView


class MenuView(TemplateView):
    template_name = 'menu.html'


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = "/login"
    template_name = "signup.html"


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "login.html"


class CreateNewForm(forms.Form):
    description = forms.CharField(label='Description', max_length=1024)


class HomeView(View):

    def get(self, request):
        context = {}
        if request.user.is_authenticated:
            context['user'] = request.user
            create_new_form = CreateNewForm()
            context['form'] = create_new_form
        return render(request, "home.html", context=context)
