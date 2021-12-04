from django.shortcuts import render, redirect
from django.views import View
from TA_Scheduler.models import User


# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        noSuchUser = False
        badPassword = False
        try:
            m = User.objects.get(username=request.POST['username'])
            print(m)
            badPassword = (m.password != request.POST['password'])
        except:
            noSuchUser = True
        if noSuchUser | badPassword:
            return render(request, "login.html", {"message": "invalid login"})
        else:
            return redirect("/home/")  # Still Deciding on what will be post-login page


class Home(View):
    def get(self, request):
        return render(request, "homeView.html", {})


class Courses(View):
    def get(self, request):
        return render(request, "courses.html", {})


class Users(View):
    def get(self, request):
        return render(request, "users.html", {})
