from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {'count': count})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def secret1(request):
    return render(request, 'secret.html')

class Secret2(LoginRequiredMixin, TemplateView):
    template_name = 'secret2.html'
