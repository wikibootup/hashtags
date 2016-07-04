from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView

from accounts.forms import LoginForm


def login(request):
    return render(request, 'accounts/login.html')


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        return super(LoginView, self).form_valid(form)
