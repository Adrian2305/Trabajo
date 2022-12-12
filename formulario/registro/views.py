from django.shortcuts import render, include, redirect
from .models import Register
from django.views.generic import View, TemplateView, FormView
from .forms import PersonForm

class CreatePerson(FormView):
    model = Register
    form_class = PersonForm
    template_name = "form.html"

# GUARDANDO INFORMACIÓN
    def form_valida(self, form):
        Register.objects.create(**form.cleaned_data)
        return redirect('index')        