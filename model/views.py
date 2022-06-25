from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User



def start(request):
    return render(request,'index.html')


def login(request):
    if request.method =='POST':
        uname= request.POST['uname']
        pas =request.POST['pas']
        user =auth.authenticate(username =uname,password =pas)
        if user is not None:
            auth.login(request,user)

            return redirect('/')
        else:
            return render(request,'login.html',{'msg':'Invalid userid'})
    else:
        return render(request,'login.html')




def register(request):
    if request.method ==  'POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        mail = request.POST['mail']
        pas = request.POST['pas']
        repas = request.POST['repas']

        if pas ==repas and pas !='':
            if User.objects.filter(username=uname).exists() or User.objects.filter(email =mail).exists():
                return render(request,'register.html',{'msg':'User name or email already taken'})
            else:
                user = User.objects.create_user(username =uname,first_name =fname,last_name = lname,email =mail,password =pas)
                user.save()
                auth.login(request,user)
                return redirect('/')
        else:
            return render(request,'register.html',{'msg':'Invalid password'})
    else:
        return render(request,'register.html')




def login2(request):
    uname= request.POST['uname']
    pas =request.POST['pas']
    user =auth.authenticate(username =uname,password =pas)
    if user is not None:
        auth.login(request,user)

        return redirect('/')
    else:
        return render(request,'login.html',{'msg':'Invalid userid'})

def register2(request):
    uname = request.POST['uname']
    fname = request.POST['fname']
    lname = request.POST['lname']
    mail = request.POST['mail']
    pas = request.POST['pas']
    repas = request.POST['repas']

    if pas ==repas and pas !='':
        if User.objects.filter(username=uname).exists() or User.objects.filter(email =mail).exists():
            return render(request,'register.html',{'msg':'User name or email already taken'})
        else:
            user = User.objects.create_user(username =uname,first_name =fname,last_name = lname,email =mail,password =pas)
            user.save()
            auth.login(request,user)
            return redirect('/')
    else:
        return render(request,'register.html',{'msg':'Invalid password'})


def logout(request):
    auth.logout(request)

    return redirect('/')

    

