from django.urls import path
from .import views
from Account.views import HomeView,LoginView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('login_here/', LoginView.as_view(), name='login'),
    path('register_here/', views.signup, name='register'),

]
