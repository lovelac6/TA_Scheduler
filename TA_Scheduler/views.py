from django.shortcuts import render, redirect
from django.views import View
from TA_Scheduler.models import User, Course, CourseAssignment


# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        noSuchUser = False
        badPassword = False
        try:
            m = User.objects.get(username=request.POST['username'])
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

class CreateUser(View):
    def get(self, request):
        return render(request, "createuser.html", {})

    def post(self, request):
        noSuchUser = False
        try:
            b = User.objects.get(username=request.POST['username'])
        except:
            noSuchUser = True
        if noSuchUser:
            b = User(username=request.POST['username'], password=request.POST['password'],
                     accountType=request.POST['type'])
            b.save()
            return redirect("/createuser/")
        else:
            return render(request, "createuser.html", {"message": "invalid login"})

class CreateCourse(View):
    def get(self, request):
        return render(request, "createcourse.html", {})

    def post(self, request):
        badNumber = False
        try:
            a = Course.objects.get(name=request.POST['coursename'])
            badNumber = (a.number != request.POST['number'])
        except:
            badNumber = True
        if badNumber:
            a = Course(name=request.POST['coursename'], number=request.POST['number'])
            a.save()
            return redirect("/createcourse/")
        else:
            return render(request, "createcourse.html", {"message": "Class Number Taken"})


