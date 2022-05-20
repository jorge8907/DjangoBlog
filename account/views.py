
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def user_login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        #User.objects.create_user("jcandamil", "jlca@email.com", "12345")
        user = authenticate(request, username=username, password=password) #Si no existe el usuario, el valor en None
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/")
            else:
                return render(request, 'auth/login.html', {
                    "error": True,
                    "message": "Disable account"
                })
        else:
            return render(request, 'auth/login.html', {
                "error": True,
                "message": "Invalid Credentials"
            })
    return render(request, 'auth/login.html')
def user_signup(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        email = request.POST['email']

        if password_confirmation!=password:
            return render(request, "auth/signup.html", {
                "error": True,
                "message": "Password and password confirmation does not match"
            })

        try:
            new_user = User.objects.create_user(username,email,password)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()
            login(request,new_user)
            return redirect("/")

        except IntegrityError:
            return render(request,"auth/signup.html",{
                "error":True,
                "message": "Email or username already registered"
            })

    return render(request, "auth/signup.html")