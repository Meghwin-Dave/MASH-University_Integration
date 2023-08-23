from email import message
from http.client import HTTPResponse
import logging
from .models import *
from multiprocessing import AuthenticationError
from pickle import NONE
from django.http import request
from django.contrib.auth.models import User, auth
from django.contrib.auth import *
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.shortcuts import render,redirect
from django.utils import regex_helper
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

data = {
    'acc_page' : ['login_page', 'register_page', 'forgot_pwd_page', 'sign_ins', 'sign_up', 'sign_inf', 'comingsoon', 'error', 'hod', 'invalidcredentials', 'forgot'],
    'roles': Role.objects.all()
}

def index(request):
    data['current_page'] = 'index'
    return render(request,'index.html',data)

def forgot_password(request):
    data['current_page']='forgot_password'
    return render(request, "forgot-password.html",data)

def sign_up(request):
    data['current_page']='sign_up'
    return render(request,'sign_up.html',data)

def sign_inf(request):
    data['current_page']='sign_inf'
    return render(request,'sign_inf.html',data)

def sign_ins(request):
    data['current_page']='sign_ins'
    return render(request,'sign_ins.html',data)

def edit(request):
    data['current_page']='edit'
    return render(request,'edit.html',data)

def contactd(request):
    data['current_page']='contactd'
    return render(request,'contactd.html',data)

def feedback(request):
    data['current_page']='feedback'
    return render(request,'feedback.html',data)



def faculty(request):
    data['current_page']='faculty'
    return render(request,'faculty.html',data)

def student(request):
    data['current_page'] = 'student'
    profile_data(request)
    return render(request,'student.html',data)

def notes1(request):
    data['current_page']='notes1'
    return render(request,'notes1.html',data)

def payment(request):
    data['current_page']='payment'
    return render(request,'payment.html',data)


def papers(request):
    data['current_page']='papers'
    return render(request,'papers.html',data)

def Studentportal(request):
    data['current_page']='Studentportal'
    return render(request,'result.html',data)

def GTUcircular(request):
    data['current_page']='GTUcircular'
    return render(request,'GTUcircular.html',data)


def timetable(request):
    data['current_page']='timetable'
    return render(request,'timetable.html',data)


def error(request):
    data['current_page']='error'
    return render(request,'error.html',data)

def invalidcredentials(request):
    data['current_page']='invalidcredentials'
    return render(request,'invalidcredentials.html',data)

def hod(request):
    data['current_page']='hod'
    return render(request,'hod.html',data)

def comingsoon(request):
    data['current_page']='comingsoon'
    return render(request,'comingsoon.html',data)

def forgot(request):
    data['current_page']='forgot'
    return render(request,'forgot-password.html',data)

def assignments(request):
    data['current_page']='assignments'
    return render(request,'assignments.html',data)

def reference(request):
    data['current_page']='reference'
    return render(request,'reference.html',data)

def notice(request):
    data['current_page']='notice'
    return render(request,'notice.html',data)



def newsletter(request):
    if request.method == 'POST':
        email = request.POST['email']
        Master.objects.create(email=request.POST['email'])
        message.success(request, "Your are succesfully registered for our Newsletter!")
        return HTTPResponse('/')
    else:
        return HTTPResponse('404 not found') 

def feedbackf(request):
    if request.method == 'POST':
        emailf = request.POST['emailf']
        First = request.POST['First']
        Subject = request.POST['Subject']
        Last = request.POST['Last']
        Feedback = request.POST['Feedback']
        enrollmentf = request.POST['enrollmentf']
       
        
        
        return HTTPResponse('/feedback')
    
def logout(request):
    auth_logout(request)
    return render(request,"index.html")
        
@csrf_exempt
def assignment_upload(request):
    master = Master.objects.get(Email = request.session['email'])
    faculty_obj = Faculty.objects.get(Master = master)
    assign = Assign.objects.create(Faculty = faculty_obj)

    if 'assign_image' in request.FILES:
        assign.assign = request.FILES['assign_image']
    
    assign.save()

    return redirect(faculty)

@csrf_exempt
def video_upload(request):
    master = Master.objects.get(Email = request.session['email'])
    faculty_obj = Faculty.objects.get(Master = master)
    video = Video.objects.create(Faculty = faculty_obj)

    if 'assign_video' in request.POST:
        video.video = request.POST['assign_video']
    
    video.save()

    return redirect(faculty)

@csrf_exempt
def notices(request):
    master = Master.objects.get(Email = request.session['email'])
    faculty_obj = Faculty.objects.get(Master = master)
    note = Note.objects.create(Faculty = faculty_obj)

    if 'data_cc' in request.POST:
        note.note = request.POST['data_cc']
    
    note.save()

    return redirect(faculty)

@csrf_exempt
def register(request):
    print(request.POST)
    role = Role.objects.get(id=int(request.POST['role']))

    # if role.Role.lower() == 'student':

    Master.objects.create(
        Role = role,
        #Role = request.POST['Role'],
        Email = request.POST['Email'],
        Password = request.POST['Password']
    )
    return redirect(sign_ins)

    
@csrf_exempt
def logins(request):
    print (request.POST)
    
    try:
        master = Master.objects.get(Email = request.POST['Email'], Password = request.POST['Password'])
        request.session['email'] = master.Email
           
        # if Master.Password == request.POST['Password']:
        return redirect(student)
            
    
        #else:
         #   raise Exception('Incorrect Password')
    except Master.DoesNotExist as err:
        print('Master Error: ', err)
    except Exception as err:
        print('Raised Error: ', err)

    return redirect(invalidcredentials)
    
def loginf(request):
    print (request.POST)
    
    try:
        master = Master.objects.get(Email = request.POST['email'],)
        if  master.Password == request.POST['password']:
            request.session['email']=master.Email
            return redirect(faculty)
        
        else:
            raise Exception('Incorrect Password')
    except User.DoesNotExist as err:
        print('User Error: ', err)
    except Master.DoesNotExist as err:
        print('Master Error: ', err)
    except Exception as err:
        print('Raised Error: ', err)

    return redirect(error)
    
def profile_data(request, to="st"):
    master = Master.objects.get(Email = request.session['email'],)
    data['user_role'] = master.Role.Role
    data['profile_data'] = master

    if to == 'st':
        data['assignments'] = Assign.objects.all()[::-1]
        data['notice'] = Note.objects.all()[::-1]
        

    elif to == 'fc':
        faculty = Faculty.objects.get(Master=master)
        data['assignments'] = Assign.objects.filter(Faculty=faculty)[::-1]
        data['notice'] = Note.objects.filter(Faculty=faculty)[::-1]
       