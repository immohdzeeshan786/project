from django.shortcuts import render

# Create your views here.
from django.shortcuts import render 
from .models import *

# Create your views here.

#view for register page 
def RegisterPage(request):
    return render(request,"app/register.html")

# View for user registration 
def UserRegister(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        contact=request.POST['contact']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        # First we will validate that user already exist
        user=User.objects.filter( Email=email)

        if user:
            messsg=" User Already exist "
            return render(request,"app/register.html",{'msg':messsg})
        else:
            if password==cpassword:
                newuser=User.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
                messsg="User Register Successfully"
                return render(request,"app/login.html",{'msg':messsg})
            else:
                messsg="Password and Confirm Password does not Match"
                return render(request,"app/register.html",{'msg':messsg})

 # Login View           
def LoginPage(request):
    return render(request,"app/login.html")

#  Login User
def LoginUser(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']

        # Checking the email with database
        user=User.objects.get(Email=email)
        if user:
            if user.Password==password:
                # We are getting user data in session
                request.session['Firstname'] = user.Firstname
                request.session['Lastname'] = user.Lastname
                request.session['Email'] = user.Email
                return render(request,"app/home.html")
            else:
                messsg="Password does not match"
                return render(request,"app/login.html",{'msg':messsg})
        else:
            messsg="user does not exist"
            return render(request,"app/register.html",{'msg':messsg})
