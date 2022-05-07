from django.shortcuts import render
from django.views.generic import CreateView
from accounts.form import SingUpForm
from django.urls import reverse_lazy

class UserCreationView(CreateView):
    form_class=SingUpForm
    success_url=reverse_lazy("login")
    template_name="accounts/singup.html"