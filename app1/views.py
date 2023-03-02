from django.shortcuts import render,redirect
from django.contrib import messages
from.forms import SignUpForms,LoginForms,ChangePasswordForms,UpdateForms
from.models import SignUp,Gallery
from django.contrib.auth import logout as logouts
def index(request):
    return render (request,'index.html')

# Create your views here.
def signup(request):
    if request.method=='POST':
        form=SignUpForms(request.POST or None,request.FILES or None)
        if form.is_valid():
            name=form.cleaned_data['Name']
            place=form.cleaned_data['Place']
            photo=form.cleaned_data['Photo']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            confirmpassword=form.cleaned_data['Confirmpassword']

            user=SignUp.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,'email already exists')
                return redirect('/signup')
            elif password!=confirmpassword:
                messages.warning(request,'password mismatch')
                return redirect('/signup')
            else:
               tab=SignUp(Name=name,Place=place,Photo=photo,Email=email,Password=password)
               tab.save()
               messages.success(request,'data saved')
               return redirect('/')
    
    else:
        form=SignUpForms()
        return render (request,'signup.html',{'form':form})  
    

def login(request):
    if request.method=='POST':
        form=LoginForms(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
        try:
            user=SignUp.objects.get(Email=email)

            if not user:
                messages.warning(request,'email does not exist')
                return redirect('/login')
            elif password!=user.Password:
                messages.warning(request,'password incorrect')
                return redirect('/login')
            else:
                messages.success(request,'login success')
                return redirect('/home/%s' %user.id)
        except:
            messages.warning(request,'email incorrect')  
            return redirect('/login')  
    else:
        form=LoginForms()
    return render (request,'login.html',{'form':form})

def home(request,id):
    user=SignUp.objects.get(id=id)
    return render(request,'home.html',{'user':user})

def changepassword(request,id):
    user=SignUp.objects.get(id=id)
    if request.method=='POST':
        form=ChangePasswordForms(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['Oldpassword']
            newpassword=form.cleaned_data['Newpassword']
            confirmpassword=form.cleaned_data['Confirmpassword']
            if oldpassword!=user.Password:
                messages.warning(request,'password incorrect')
                return redirect('/changepassword/%s' %user.id)
            elif oldpassword==newpassword:
                messages.warning(request,'password similar')
                return redirect('/changepassword/%s' %user.id)
            else: 
                user.Password==newpassword
                user.save()
                messages.success(request,'password changed')
                return redirect('/home/%s' %user.id)
    else:
        form=ChangePasswordForms()
        return render(request,'changepassword.html',{'form':form})

def logout(request):
    logouts(request)
    messages.success(request,'logout')
    return redirect('/')

def update(request,id):
    user=SignUp.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForms(request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'data updated')
            return redirect('/home/%s' %user.id)

    else:
        form=UpdateForms(instance=user)
        return render(request,'update.html',{'form':form})



def gallery(request):
    image=Gallery.objects.all()
    return render(request,'gallery.html',{'image':image})

def detail(request,id):
    user=Gallery.objects.get(id=id)
    return render(request,'details.html',{'user':user})