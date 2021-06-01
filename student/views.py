from django.shortcuts import render,redirect
from .models import Registration,Subscribe,Contact,Admission,Comment,Fqu,Cources,Cart,Specific_Crc
from django.contrib import messages
from django.http import HttpResponse
import smtplib, ssl
import random

# Create your views here.

# Main Page...

def index(request):
    data = Specific_Crc.objects.all()
    if request.method == "POST":
        data=Subscribe()
        data.Email=request.POST['email']
        data.save()
    return render(request,'index.html',{'data':data})

# User Login......

def login(request):
    data = Specific_Crc.objects.all()
    if request.method == "POST":
        try:
            Email = request.POST['Email']
            print(Email)
            KML='True'
            KML=request.POST.get('KML','')=='on'
            Password = request.POST['Password']
            data=Registration.objects.get(Email=Email)
            print(data)
            if data.Password == Password:
                if KML == True:
                    request.session['Email'] = Email
                print(KML)
                return redirect('index')
            else:
                messages.warning(request, "Wrong Password")
        except:
            messages.error(request,'User Not Found')
    return render(request,'login.html',{'data':data})

# Forgot Password.........

def forgot_pass(request):
    data = Specific_Crc.objects.all()
    Email = request.POST.get('Email')
    request.session['Email'] = Email
    if Email == None:
        return render(request,'email.html')

        
    print(Email)
    otp = ''
    rand = random.choice('0123456789')
    rand1 = random.choice('0123456789')
    rand2 = random.choice('0123456789')
    rand3 = random.choice('0123456789')
    otp = rand + rand1 + rand2 + rand3
    print(otp)
    request.session['otp'] = otp


    port = 465
    password = "Neek@031"
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com",port,context=context)
    server.login("patelkirti1720@gmail.com",password)
    server.sendmail("patelkirti1720@gmail.com",Email,otp)
    server.quit()
    return redirect('otpcheck')
        

    return render(request,'email.html')

# OTP Checked.......    

def otpcheck(request):
    data = Specific_Crc.objects.all()
    if request.session.has_key('otp'):
        otp = request.session['otp']
        try:
            otpobj = request.POST.get('otp')
            if otpobj == None:
                return render(request,'otp.html')
            if otp == request.POST.get('otp'):
                return redirect('newpassword')
            else:
                return HttpResponse("<a href = ''>Wrong OTP Entered.</a>")
        except:
            return redirect('login')
    return render(request,'otp.html')

# New Password.............

def newpassword(request):
    data = Specific_Crc.objects.all()
    new_pass = request.POST.get('password')
    if new_pass == None:
        return render(request,'forgotpassword.html')
    obj = Registration.objects.get(Email = request.session['Email'])
    obj.Password = new_pass
    obj.CPassword=new_pass
    obj.save()
    if request.session.keys():
        request.session.flush()
        return redirect('login')
    return render(request,'forgotpassword.html')


# User Logout........

def logout(request):
    data = Specific_Crc.objects.all()
    if request.session.keys():
        request.session.flush()
        return redirect('login')
    else:
        return render(request, 'index.html',{'data':data})

# Contact Page........

def contact(request):
    data = Specific_Crc.objects.all()
    if request.method=="POST":
        data=Contact()
        data.FstName=request.POST['FstName']
        data.LstName=request.POST['LstName']
        data.Subject=request.POST['Subject']
        data.Email=request.POST['Email']
        data.Message=request.POST['Message']
        data.save()
    return render(request,'contact.html',{'data':data})

# About Page.........

def about(request):
    data = Specific_Crc.objects.all()
    return render(request,'about.html',{'data':data})

def course_details(request):
    data = Specific_Crc.objects.all()
    return render(request,'course_details.html',{'data':data})

# Admission Page........

def form(request):
    data = Specific_Crc.objects.all()
    if 'Email' in request.session:
        tc=Registration.objects.get(Email=request.session['Email'])
        if request.method == "POST" or request.FILES:
            data=Admission()
            data.FstName=request.POST['FstName']
            data.MidName=request.POST['MidName']
            data.LstName=request.POST['LstName']
            data.Dob=request.POST['date']
            data.Gender=request.POST['Gender']
            data.Country=request.POST['Country']
            data.Phone=request.POST['Phone']
            data.Email=tc
            data.Address=request.POST['Address']
            data.Line=request.POST['Line']
            data.City=request.POST['City']
            data.State=request.POST['State']
            data.Code=request.POST['Code']
            data.Course=request.POST['Course']
            data.AdharCard=request.POST and request.FILES['AdharCard']
            data.Passport=request.POST and request.FILES['Passport']
            data.Fmarksheet=request.POST and request.FILES['Fmarksheet']
            data.Smarksheet=request.POST and request.FILES['Smarksheet']
            data.Signature=request.POST and request.FILES['Signature']
            data.Payment=request.POST['Payment']
            data.save()
            return redirect('applyform')
    else:
        return redirect('login')
    return render(request,'Admission.html',{'tc':tc,'data':data})

# 404 error Page ........ 

def error(request):
    data = Specific_Crc.objects.all()
    return render(request,'404.html',{'data':data})


def link(request):
    data = Specific_Crc.objects.all()
    return render(request,'link.html',{'data':data})

# Blog Page..........

def blog(request):
    data = Specific_Crc.objects.all()
    return render(request,'blog.html',{'data':data})

# Coming_soon Page

def coming_soon(request):
    data = Specific_Crc.objects.all()
    if request.method == "POST":
        data=Subscribe()
        data.Email=request.POST['email']
        data.save()
    return render(request,'coming_soon.html',{'data':data})

# Faq Page...........

def faq(request):
    data = Specific_Crc.objects.all()
    return render(request,'faq.html',{'data':data})

# Gallary

def gallery(request):
    data = Specific_Crc.objects.all()
    return render(request,'gallery.html',{'data':data})

# Home Page........

def index2(request):
    data = Specific_Crc.objects.all()
    return render(request,'index-2.html',{'data':data})

# Register Page.............

def register(request):
    data = Specific_Crc.objects.all()
    if request.method == "POST":
        data=Registration()
        data.Name=request.POST['Name']
        data.Email=request.POST['Email']
        data.Password=request.POST['Password']
        data.CPassword=request.POST['CPassword']
        data.TNC='True'
        data.TNC=request.POST.get('TNC','')=='on'
        data.save()
        return redirect('login')
    return render(request,'register.html',{'data':data})


# Comment Page..............

def single(request):
    data = Specific_Crc.objects.all()
    tc=Registration.objects.get(Email=request.session['Email'])
    if request.method == "POST":
        data=Comment()
        data.Name=request.POST['Name']
        data.Email=tc
        data.Comment=request.POST['Message']
        data.save()
    return render(request,'single.html',{'data':data})

# Admin Login........

def admin(request):
    data = Specific_Crc.objects.all()
    if request.method == "POST":
        try:
            Email = request.POST['Email']
            Password= request.POST['Password']
            if Email == 'k@gmail.com' and Password == '1702':
                return redirect('showadmin')
            else:
                return HttpResponse("Wrong password")
        except:
            return HttpResponse("User not found")
    return render(request, 'login.html',{'data':data})


# Show Admin Panel........

def showadmin(request):
    crc = Specific_Crc.objects.all()
    data=Registration.objects.all()
    obj=Contact.objects.all()
    return render(request,'showadmin.html',{'data':data,'obj':obj,'crc':crc})

# Show Contact..........

def showcontact(request):
    data = Specific_Crc.objects.all()
    obj=Contact.objects.all()
    return render(request,'showcontact.html',{'obj':obj,'data':data})

# Show Comment........

def showcomment(request):
    crc = Specific_Crc.objects.all()
    data=Comment.objects.all()
    return render(request,'showcomment.html',{'data':data,'crc':crc})

# Show Subscribe.........   

def showsubscribe(request):
    crc = Specific_Crc.objects.all()
    data=Subscribe.objects.all()
    return render(request,'showsubscribe.html',{'data':data,'crc':crc})

# Show Apply Form..............

def applyform(request):
    if 'Email' in request.session:
        user = Registration.objects.get(Email=request.session['Email'])
        data = Admission.objects.filter(Email=user,Approved='Approved')
        if data:
            return redirect('Aprove')
        else:
            return redirect('Disaprove')
    # return render(request, 'conformform.html', {'data': data})

# Approve Form.............

def Aprove(request):
    if 'Email' in request.session:
        user = Registration.objects.get(Email=request.session['Email'])
        data = Admission.objects.filter(Email=user,Approved='Approved')
    return render(request, 'conformform.html', {'data': data})

# Disaprove Form........

def Disaprove(request):
    if 'Email' in request.session:
        user = Registration.objects.get(Email=request.session['Email'])
        data = Admission.objects.filter(Email=user)
        if data:
            return render(request, 'Pendingform.html')
        else:
            return render(request,'plsapply.html')


# Edit Apply Form..........

def editapply(request,id):
    tc=Registration.objects.get(Email=request.session['Email'])
    data=Admission.objects.get(id=id)
    if request.method=="POST" or request.FILES:        
        data.FstName=request.POST['FstName']
        data.MidName=request.POST['MidName']
        data.LstName=request.POST['LstName']
        data.Dob=request.POST['date']
        data.Gender=request.POST['Gender']
        data.Country=request.POST['Country']
        data.Phone=request.POST['Phone']
        data.Email=tc
        data.Address=request.POST['Address']
        data.Line=request.POST['Line']
        data.City=request.POST['City']
        data.State=request.POST['State']
        data.Code=request.POST['Code']
        data.Course=request.POST['Course']
        data.AdharCard=request.POST and request.FILES['AdharCard']
        data.Passport=request.POST and request.FILES['Passport']
        data.Fmarksheet=request.POST and request.FILES['Fmarksheet']
        data.Smarksheet=request.POST and request.FILES['Smarksheet']
        data.Signature=request.POST and request.FILES['Signature']
        data.Payment=request.POST['Payment']
        data.save()
        return redirect('applyform')
    return render(request,'editapply.html',{'data':data})

# Delete Apply Form

def deleteapply(request):
    if 'Email' in request.session:
        user = Registration.objects.get(Email=request.session['Email'])
        data = Admission.objects.filter(Email=user)
        data.delete()
        return redirect('form')
    return render(request, 'Admission.html')


# Edit & Delete User Data..........

def editadmin(request,id):
    data=Registration.objects.get(id=id)
    if request.method == "POST":
        data.Name=request.POST['Name']
        data.Email=request.POST['Email']
        data.Password=request.POST['Password']
        data.CPassword=request.POST['CPassword']
        data.TNC='True'
        data.TNC=request.POST.get('TNC','')=='on'
        data.save()
        return redirect('showadmin')
    return render(request,'editadmin.html',{'data':data})

def deleteadmin(request,id):
    data=Registration.objects.get(id=id)
    data.delete()
    return redirect('showadmin')
    return render(request,'showadmin.html',{'data':data})

# Add Languages....

def course(request,title):
    lang =Specific_Crc.objects.get(title=title)
    if request.method == "POST" or request.FILES:
        data = Cources()
        data.Book_lang = request.POST['language']
        data.cat = lang
        data.Book_price = request.POST['Price']
        data.Book_desc= request.POST['discription']
        data.Book_img= request.POST and request.FILES['img']
        data.save()
        return redirect('index')
    return render(request, 'showcourse.html', {'lang':lang})

# Category....

def Catgry(request,title):
    data = Specific_Crc.objects.all()
    m = Specific_Crc.objects.get(title=title)
    p = Cources.objects.filter(cat=m)
    title=m
    print(title)
    return render(request,'catgry.html',{'data':data,'p':p,'title':title})

# Add Cart........

def addtocart(request, id):
    if 'Email' in request.session:
        m = Registration.objects.get(Email=request.session['Email'])
        pro = Cources.objects.get(id=id)
        if request.method == "POST":
            c = Cart()
            c.Email = m
            c.Books = pro
            c.Quantity = request.POST['quentity']
            c.Price = (pro.Book_price) * float(c.Quantity)
            c.save()
            return redirect('Usrcart')
        return render(request, 'addcart.html', {'m': m, 'pro': pro})
    else:
        return redirect('login')


def Usrcart(request):
    if 'Email' in request.session:
        user = Registration.objects.get(Email=request.session['Email'])
        data = Cart.objects.filter(Email=user)
    return render(request, 'cart.html', {'data': data})

# Show Admission Data..........

def showadmission(request,Email):
    i=Registration.objects.all()
    j=Registration.objects.get(Email=Email)
    data=Admission.objects.filter(Email=j)
    print(Email)
    return render(request,'Showadmission.html',{'data':data})

# Aprove Data...............

def Approved(request,Email):
    i=Registration.objects.all()
    j=Registration.objects.get(Email=Email)
    data=Admission.objects.filter(Email=j).update(Approved="Approved")
    return redirect('showadmin')