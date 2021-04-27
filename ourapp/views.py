from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import NewUserForm
from django.contrib import messages 


# Create your views here.
def index (request):
    #return HttpResponse ("Hello")
    if not request.user.is_authenticated:
        return render (request, "ourapp/login.html", {"message": None})
    context = {"user": request.user}
    return render (request, "ourapp/user.html", context)

def register_view(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("git initlogin")  
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, template_name="register.html", context={"register_form":form})

def login_view(request):
    if request.method  == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render (request, "ourapp/login.html", {"message": "invalid credentials"})
    return render(request, 'ourapp/login.html')         

def logout_view(request):
    logout(request)
    return render (request, "ourapp/login.html", {"message": "logged out"})
    # else: 
    #     return render (request, "ourapp/login.html", {"message": "invalid credentials"})