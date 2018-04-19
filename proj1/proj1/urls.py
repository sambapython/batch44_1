"""proj1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#from django.http import HttpResponse
from app1.views import view_users, view_home
'''
def view_users(request):
	#return HttpResponse("Hello client. How are you doing!!")
	#return "Hello client. How are you doing!!"
	return HttpResponse("<h1>Hello client. How are you doing!!</h1>")
'''

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', view_users),
    url(r'^home/', view_home),
]
