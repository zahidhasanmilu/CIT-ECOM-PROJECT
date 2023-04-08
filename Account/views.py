from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


# Create your views here.
class HomeView(View):
    template_name = 'Account/index.html'

    def get(self, request):

        context = {

        }
        return render(request, self.template_name)

class signin(View):
    template_name = 'Account/user-login.html'


    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user, 'Hello')
        if user:
            login(request, user)
            print("User logged in Successfully")
            return redirect('home')
        else:
            messages.info(request, "User Doesn't Exists")
            return redirect('login')

def forgotpassword(request):
    if request.method=='POST':
        usernames = request.POST["username"]
        email = request.POST["email"]
        new_password = request.POST["new_password"]

        user = User.objects.get(username=usernames)
        if user :            
            if user.email == email:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                messages.info(request, "Password Update succecfully")
                return redirect('login')
            else:
                messages.info(request, "Email Not Matched")
                return redirect('forgotPassword')
        else:
            messages.info(request, "User Not Found")
            return redirect('forgotPassword')

    return render(request, 'Account/forgotpassword.html')

# def signin(request):
#     print('Zahid')
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         print(username, password)
#         user = authenticate(username=username, password=password)
#         print(user, 'Hello')
#         if user:
#             login(request, user)
#             print("User logged in succecfully")
#             return redirect('home')
#         else:
#             messages.info(request, "User Doesn't Exists")
#             return redirect('login')
#     return render(request, 'Account/user-login.html')



def signout(request):
    logout(request)
    messages.info(request, "Logout Successfully")
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User Already Exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exists")
                return redirect('register')
            else:
                obj = User.objects.create_user(
                    username=username, email=email, password=password)
                obj.set_password(password)
                obj.save()
                messages.success(request, 'User Create Successfully')
                return redirect('login')
        else:
            messages.info(request, "password doesn't match")
            return redirect('register')
    return render(request, 'Account/user-register.html')


class AboutView(View):
    template_name = 'Account/page-about-us.html'

    def get(self, request):
        return render(request, self.template_name)


class ContactUsView(View):
    template_name = 'Account/page-contact.html'

    def get(self, request):
        return render(request, self.template_name)
