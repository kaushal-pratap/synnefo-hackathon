from django.shortcuts import render,HttpResponse,redirect
from .models import image_collection,db
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.conf import settings
from pymongo import MongoClient
from bson.binary import Binary
from PIL import Image
from django.contrib.auth.decorators import login_required
import io
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/loginUser')
    return render(request,'index.html')
def add_person(request):
    records = {
        "first_name" : "CEO",
        "last_name" : "Kaushal"
    }
    # code below to create a new collection(user)
    # db.create_collection("User1")
    image_collection.insert_one(records)
    return HttpResponse("New person is added")

def get_all_person(request):
    persons = image_collection.find()
    return HttpResponse(persons)
@login_required(login_url='/loginUser/')  # Redirects to login page if not logged in

def about(request):
    return(
        HttpResponse("This is about page")
    )
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #check if user has entered correct credentials or not
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,'login.html')
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return HttpResponse("Logged out successfully")

def createUser(request):
    try:
        if request.method=='POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            db.create_collection(username)
            return HttpResponse("User created successfully")
    except:
        return HttpResponse("Error creating user")
    return render(request,"register.html")

def uploadFile(request):
    if request.method == 'POST':
        return HttpResponse('image_upload_success')
    return render(request, 'index.html')


def image(request):
    return render(request, 'image.html')
# def uploadFile
# views.py


