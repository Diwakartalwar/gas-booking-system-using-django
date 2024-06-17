from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from .models import *


def index(request):
    return render(request,'index.html')

def login(request):
    error=""
    if request.method=="POST":
        u = request.POST['uname']
        p = request.POST['pswd']
        user = auth.authenticate(username=u,password=p)
        try:
            if user.is_staff:
                auth.login(request,user)
                error="no"
            elif user is not None:
                auth.login(request,user)
                error="user"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'login.html',d)


def admin_home(request):
    return render(request,'admin_home.html')

def booking(request):
    data = Booking.objects.all()
    d = {'data':data}
    return render(request,'bookings.html',d)

def user(request):
    data = Registration.objects.all()
    d = {'data':data}
    return render(request,'users.html',d)

def signup(request):
    error=""
    if request.method=="POST":
        n = request.POST['fname']
        e = request.POST['email']
        c = request.POST['contact']
        p = request.POST['pswd']
        a = request.POST['aadhar']
        ct = request.POST['city']
        try:
            user = User.objects.create_user(username=e,password=p)
            Registration.objects.create(user=user,fullname=n,mobile=c,aadhar=a,city=ct)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'signup.html',d)

def user_home(request):
    user = request.user
    data = Registration.objects.get(user=user)
    d = {'data':data}
    return render(request,'user_home.html',d)


def Logout(request):
    logout(request)
    return redirect('index')

def book_now(request):
    error=""
    if request.method=="POST":
        n = request.POST['fname']
        c = request.POST['contact']
        bd = request.POST['bdate']
        t = request.POST['type']
        p = request.POST['price']
        a = request.POST['address']
        e = request.user
        try:
            Booking.objects.create(fullname=n,contact=c,booking_date=bd,type=t,
                                   email=e,price=p,address=a,status="Pending")
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'book_now.html',d)

def my_booking(request):
    e = request.user
    print(e)
    data = Booking.objects.filter(email__icontains=e)
    d = {'data':data}
    return render(request,'my_booking.html',d)


def delete_booking(request,id):
    data = Booking.objects.get(id=id)
    data.delete()
    return redirect('booking')

def change_status(request,id):
    error = ""
    data = Booking.objects.get(id=id)
    if request.method=="POST":
        s = request.POST['status']
        data.status=s
        try:
            data.save()
            error="no"
        except:
            error="yes"
    d = {'error':error,'data':data}
    return render(request,'change_status.html',d)

def delete_user(request,id):
    data = User.objects.get(id=id)
    data.delete()
    return redirect('user')

def feedback(request):
    error=""
    if request.method=='POST':
        n = request.POST['name']
        e = request.POST['email']
        c = request.POST['contact']
        f = request.POST['feedback']
        try:
            Feedback.objects.create(name=n,email=e,contact=c,feedback=f)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'feedback.html',d)


def view_feedback(request):
    data = Feedback.objects.all()
    d = {'data':data}
    return render(request,'view_feedback.html',d)


def delete_feedback(request,id):
    data = Feedback.objects.get(id=id)
    data.delete()
    return redirect('view_feedback')

def about(request):
    return render(request,'about.html')
