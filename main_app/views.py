from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import UserProfile, Posts
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.

class Home(View):
    
    def get(self, request):
        return HttpResponse("Wayfarer Home")


class Home(TemplateView):
    template_name = "home.html"

@method_decorator(login_required, name='dispatch')
class UserProfileList(TemplateView):
    template_name = "profile_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Here we are using the model to query the database for us.
        context["profiles"] = UserProfile.objects.all()
        return context

class PostsList(TemplateView):
    template_name = "profile_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Posts.objects.all() # Here we are using the model to query the database for us.
        return context

      




class Signup(View):

    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_list")
        else:
            return redirect("signup")
