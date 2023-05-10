from django.urls import path
from Accounts import views


app_name = 'Accounts'

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('unauth', views.unauth, name='unauth'),
]