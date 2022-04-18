from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):
    if request.POST.get("num4",False):
        usr=request.POST["num1"]
        eml=request.POST["num2"]
        psw=request.POST["num3"]
        if User.objects.filter(username=usr).exists():
            messages.info(request, 'Username Taken')
            return render(request,'index.html')
        elif User.objects.filter(email=eml).exists():
            messages.info(request, 'Email Taken')
            return render(request,'index.html')
        else:
            user= User.objects.create_user(username=usr,email=eml,password=psw)
            user.save()
            print('user created')
            return render(request,'login.html')
        #return redirect('/')
    else:
        return render(request,'index.html')
def login(request):
    if request.method=='POST':
        username = request.POST['num1']
        password= request.POST['num2']
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'result.html',{'name':user.first_name})
        else:
            messages.info(request,'invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def result(request):
    if request.POST.get('res',False):
        data1=request.POST['data1']
        data2=request.POST['data2']
        op=int(data1)+int(data2)
        return render(request,'result.html',{'output':op,'res':True})
    else:
        return render(request,'result.html')
def logout(request):
    auth.logout(request)
    return redirect('/')