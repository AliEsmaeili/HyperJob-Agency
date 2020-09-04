from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.views import View
from django.views.generic.base import TemplateView
from .models import Vacancy
from hyperjob.views import CreateNewForm

# Create your views here.
class VacanciesView(TemplateView):
    template_name = 'vacancy/vacancies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.all()
        return context


class NewVacancyView(View):

    def post(self, request):
        create_new_form = CreateNewForm(request.POST)
        if create_new_form.is_valid() and request.user.is_authenticated and request.user.is_staff:
            description = create_new_form.cleaned_data['description']
            Vacancy.objects.create(description=description, author=request.user)
            return redirect('/home')
        return HttpResponseForbidden()
