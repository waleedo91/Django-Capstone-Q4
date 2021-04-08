from django.views.generic import View
from .forms import SignUpForm
from django.shortcuts import render, reverse, redirect
from django.contrib.auth import login
# from .models import Player
from django.contrib.auth.models import User

# Create your views here.

class RegisterView(View):
    html = "signup.html"

    def get(self, request):
        template_name = "signup.html"
        form = SignUpForm()
        return render(request, template_name, {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
            username=data.get("username"), password=data.get("password1")
             )
            login(request, user)
            return redirect(reverse("login"))

