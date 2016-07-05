from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy

from accounts.forms import LoginForm


def login(request):
    return render(request, 'accounts/login.html')


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super(LoginView, self).form_valid(form)
