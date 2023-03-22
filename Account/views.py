from django.shortcuts import render
from django.views.generic import View


# Create your views here.
class HomeView(View):
    template_name = 'Account/index.html'
    template_name2 = 'Account/index.html'

    def get(self,request):
    

        context={

        }
        return render(request, self.template_name )
    




class LoginView(View):
    template_name = 'Account/user-login.html'
    template_name2 = 'Account/index.html'

    def get(self, request):
        return render(request, self.template_name)



def signup(request):
    return render(request, 'Account/user-register.html')


class AboutView(View):
    template_name = 'Account/page-about-us.html'

    def get(self,request):
        return render(request, self.template_name )

class ContactUsView(View):
    template_name = 'Account/page-contact.html'

    def get(self,request):
        return render(request, self.template_name )