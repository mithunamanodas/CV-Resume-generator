from django.shortcuts import render
from.models import *
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io

# Create your views here.

def home(request):
    return render(request,'home.html')

def user_details(request):
    username = request.session['username']
    user_name=Signup.objects.get(username=username)
    name=request.POST['name']
    phone=request.POST['phone']
    email=request.POST['email']
    school=request.POST['school']
    mark1=request.POST['mark1']
    degree=request.POST['degree']
    university=request.POST['university']
    mark2=request.POST['mark2']
    skills=request.POST['skills']
    about_you=request.POST['about_you']
    previous_work=request.POST['previous_work']
    data=Profile(username=user_name,name=name,phone=phone,email=email,school=school,degree=degree,mark1=mark1,university=university,mark2=mark2,skills=skills,about_you=about_you,previous_work=previous_work)
    data.save()
    return render(request ,'accept.html')

def accept(request):
    return render(request ,'accept.html')


def list_download(request):
    username = request.session['username']
    user_name=Signup.objects.get(username=username)
    profile=Profile.objects.filter(username = user_name)
    return render(request,"list.html",{"profile":profile})

def list(request):
    # profile=Profile.object.all()
    return render(request ,'list.html')


def faq(request):
    return render(request ,'faq.html')

def user_data(request):
    username=request.POST['username']
    password=request.POST['password']
    email=request.POST['email']
    data=Signup(username=username,password=password,email=email)
    data.save()
    data1=Login(username=username,password=password,type=0)
    data1.save()
    return render(request,"index.html")


def check(request):
    username=request.POST['username']
    password=request.POST['password']
    data1=Login.objects.get(username=username,password=password)
    request.session['username']=data1.username
    request.session['password']=data1.password
    return render(request,"accept.html")
   
def index(request):
    return render(request,"index.html")

def res(request):
    username = request.session['username']
    user_name=Signup.objects.get(username=username)
    data3=Profile.objects.filter(username = user_name)
    return render(request,"resume.html",{'result_33':data3})

# def resume(request,id):
#     user_profile=Profile.objects.get(pk=id)
#     template=loader.get_template("resume.html")
#     html=template.render({'user_profile':user_profile})
#     option={
#         'page-size':'Letter',
#         'encoding':'UTF-8'
#     }
#     pdf=pdfkit.from_string(html,False,option)
#     response=HttpResponse(pdf,content_type='application/pdf')
#     response['Content-Disposition']='attachment'
#     return response

def resume(request):
    return render(request ,'resume.html')

def about_us(request):
    return render(request ,'about_us.html')

def contact(request):
    return render(request ,'contact.html')

