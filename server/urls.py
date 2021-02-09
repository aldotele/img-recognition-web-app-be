"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from authentication_app.views import login
from upload_app.views import upload
from upload_app.views import upload_test
from registration_app.views import signup


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('upload/', upload, name='upload'),
    path('upload_test/', upload_test, name='upload_test'),
    path('signup/', signup, name='signup'),
]

