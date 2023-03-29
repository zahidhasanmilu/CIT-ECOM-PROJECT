from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
class HomeView(View):
    template_name = 'Account/index.html'
    template_name2 = 'Account/index.html'

    def get(self,request):
    

        context={

        }
        return render(request, self.template_name )
    


def signin(request):
    print('Zahid')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username = username, password=password)
        print(user, 'Hello')
        if user:
            login(request, user)
            print("User logged in succecfully")
            return redirect('home')
        else:
            messages.info(request, "User Doesn't Exists")
            return redirect('login')
    return render(request, 'Account/user-login.html')



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User Already Exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exists")
                return redirect('register')
            else:
                obj = User.objects.create_user(username=username, email=email, password=password)
                obj.set_password(password)
                obj.save()
                messages.success(request, 'User Create Succefully')
                return redirect('login')
        else:
            messages.info(request, "password doesn't match")
            return redirect('register')
    return render(request, 'Account/user-register.html')


class AboutView(View):
    template_name = 'Account/page-about-us.html'

    def get(self,request):
        return render(request, self.template_name )

class ContactUsView(View):
    template_name = 'Account/page-contact.html'

    def get(self,request):
        return render(request, self.template_name )