"""portfolioProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info', views.info, name='info'),
    path('project', views.project, name='project'),
    path('write_new', views.write_new, name='write_new'),
    path('list', views.list, name='list'),
    path('list/<str:category>', views.list, name='list'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('category', views.category, name='category'),

]
