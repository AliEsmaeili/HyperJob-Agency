from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.views import View
from django.views.generic.base import TemplateView
from .models import Resume
from hyperjob.views import CreateNewForm
# Create your views here.

class ResumesView(TemplateView):
    template_name = 'resume/resumes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resumes'] = Resume.objects.all()
        return context


class NewResumeView(View):

    def post(self, request):
        create_new_form = CreateNewForm(request.POST)
        if create_new_form.is_valid() and request.user.is_authenticated and not request.user.is_staff:
            description = create_new_form.cleaned_data['description']
            Resume.objects.create(description=description, author=request.user)
            return redirect('/home')
        return HttpResponseForbidden()
