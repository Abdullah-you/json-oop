
from django.http import HttpResponse
from django.shortcuts import render, redirect
import random
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password

from signup import settings
from .forms import SignUp
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "authentication/index.html")

@login_required
def home(request):
    username = request.session.get('username')
    first_name = request.session.get('first_name')
    password = request.session.get('password')
    context = {
        "username":username,
        "first_name":first_name,
        "password":password
    }
    return render(request, "authentication/home.html", context)

def signin(request):
    if request.method == "POST":
        form = SignUp(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            #messages.success(request, "You've logged in successfully !")
            #fname = user.first_name
            #return render(request, "authentication/home.html", {'fname':fname})
            request.session['username'] = user.username
            request.session['first_name'] = user.first_name
            request.session['password'] = user.password
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials !")
            return redirect('signin')
    else:
        form = SignUp()
    return render(request, "authentication/signin.html",{'form':form})

def signup(request):
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            if not User.objects.filter(Q(username=username) | Q(email=email)):
                fname = form.cleaned_data['first_name']
                lname = form.cleaned_data['last_name']
                password = form.cleaned_data['password']
        # fname = request.POST['first_name']
        # lname = request.POST['last_name']
        # username = request.POST['username']
        # email = request.POST['email']
        # password = request.POST['password']

                myuser = User.objects.create_user(username, email, password)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save()
                return redirect("signin")
            else:
                messages.error(request, "User already exists")
                return redirect('signup')
                
    else:
        form = SignUp()
    return render(request, "authentication/signup.html", {"form":form})

def signout(request):
    logout(request)
    mes = "You've logged out successfully"
    return render(request,"authentication/index.html", {'message':mes})

# def change_password(request):
#     return render(request, "authentication/changepass.html")

def otp_gen():
    otp = random.randint(1001,9999)
    return otp

# random_otp = otp_gen() 
# def forget_password(request):
#     global random_otp
#     switch = True
#     if switch:
#         if request.method == "POST":
#             email = request.POST.get('email')
#             user = User.objects.get(email=email)
#             if user:
#                 print("user found")
#                 subject = "Forget Password Mail"
#                 message = f'Hi {user.username}, {random_otp} is your reset OTP'
#                 print(random_otp)
#                 email_from = settings.EMAIL_HOST_USER
#                 recipient_list = [user.email, ]
#                 send_mail( subject, message, email_from, recipient_list )
#                 return render(request, 'authentication/forgetpas.html', {'switch':switch})
#             else:
#                 pass
#     else:
#         switch = False
#         return render(request, "authentication/forgetpas.html", {'switch':switch})
#     return render(request, "authentication/forgetpas.html")


def forget_password(request):
    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, 'Email not found.')
                return redirect('forget-password')

            
            otp = random.randint(1001, 9999)

            
            subject = 'Password Reset OTP'
            message = f'Your OTP is: {otp}'
            from_email = settings.EMAIL_HOST_USER
            to_email = [user.email, ]
            send_mail(subject, message, from_email, to_email)

            
            request.session['password_reset_otp'] = otp
            request.session['password_reset_email'] = email

            
            return render(request, 'authentication/forget_password.html', {'otp_required': True})

    
        elif 'otp' in request.POST and 'new_password' in request.POST:
            entered_otp = request.POST['otp']
            entered_email = request.session.get('password_reset_email')

            
            if str(request.session.get('password_reset_otp')) == entered_otp and entered_email:
            
                user = User.objects.get(email=entered_email)
                new_password = request.POST['new_password']
                hashed_password = make_password(new_password)
                user.password = hashed_password
                #user.set_password = hashed_password
                user.save()

                messages.success(request, 'Password reset successful. You can now log in with your new password.')
                return redirect('signin')
            else:
                messages.error(request, 'Invalid OTP. Please try again.')
                return redirect('forget-password')
            
    return render(request, 'authentication/forget_password.html', {'otp_required': False})



