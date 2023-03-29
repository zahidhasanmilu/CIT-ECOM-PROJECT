from django.urls import path
from .import views
from Account.views import HomeView,ContactUsView,AboutView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('login_here/', views.signin, name='login'),
    path('register_here/', views.signup, name='register'),
    path('About_Us/', AboutView.as_view(), name='aboutus'),
    path('Contact_Us/', ContactUsView.as_view(), name='contactus'),

]
