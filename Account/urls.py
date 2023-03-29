from django.urls import path
from .import views
from Account.views import HomeView,ContactUsView,AboutView,signin

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    # path('login_here/', views.signin, name='login'),
    path('login/', signin.as_view(), name='login'),
    path('logount/', views.signout, name='logout'),
    path('register_here/', views.signup, name='register'),
    path('About_Us/', AboutView.as_view(), name='aboutus'),
    path('Contact_Us/', ContactUsView.as_view(), name='contactus'),

]
