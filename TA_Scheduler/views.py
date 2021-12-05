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


class CreateCourse(View):
    def get(self, request):
        return render(request, "createcourse.html", {})

    def post(self, request):
        badNumber = False
        try:
            a = Course.objects.get(coursename=request.POST['coursename'])
            badNumber = (a.number != request.POST['number'])
        except:
            badNumber = True
        if badNumber:
            a = Course(coursename=request.POST['coursename'], number=request.POST['number'])
            a.save()
            return redirect("/createcourse/")
        else:
            return render(request, "createcourse.html", {"message": "Class Number Taken"})


class Users(View):
    def get(self, request):
        return render(request, "users.html", {})
