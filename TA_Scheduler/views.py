from django.shortcuts import render, redirect
from django.views import View


# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        noSuchUser = False
        badPassword = False
        try:
            m = MyUser.objects.get(name=request.POST['name'])
            badPassword = (m.password != request.POST['password'])
        except:
            noSuchUser = True
        if noSuchUser | badPassword:
            return render(request, "login.html", {"message": "invalid login"})
        else:
            return redirect("") #Still Deciding on what will be post-login page
