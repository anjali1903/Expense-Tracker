"""project URL Configuration

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
from webapp import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', views.test),
    url(r'^checkexpense/', views.checkexpense),
    url(r'^checkexpenseJan/', views.checkexpenseJan),
    url(r'^checkexpenseFeb/', views.checkexpenseFeb),
    url(r'^checkexpenseMar/', views.checkexpenseMar),
    url(r'^checkexpenseApr/', views.checkexpenseApr),
    url(r'^checkexpenseMay/', views.checkexpenseMay),
    url(r'^checkexpenseJun/', views.checkexpenseJun),
    url(r'^checkexpenseJul/', views.checkexpenseJul),
    url(r'^checkexpenseAug/', views.checkexpenseAug),
    url(r'^checkexpenseSep/', views.checkexpenseSep),
    url(r'^checkexpenseOct/', views.checkexpenseOct),
    url(r'^checkexpenseNov/', views.checkexpenseNov),
    url(r'^checkexpenseDec/', views.checkexpenseDec),
    url(r'^landing/', views.landing),
    url(r'^addexpense/', views.addexpense),
    url(r'^addexpenseJan/', views.addexpenseJan),
    url(r'^addexpenseFeb/', views.addexpenseFeb),
    url(r'^addexpenseMar/', views.addexpenseMar),
    url(r'^addexpenseApr/', views.addexpenseApr),
    url(r'^addexpenseMay/', views.addexpenseMay),
    url(r'^addexpenseJun/', views.addexpenseJun),
    url(r'^addexpenseJul/', views.addexpenseJul),
    url(r'^addexpenseAug/', views.addexpenseAug),
    url(r'^addexpenseSep/', views.addexpenseSep),
    url(r'^addexpenseOct/', views.addexpenseOct),
    url(r'^addexpenseNov/', views.addexpenseNov),
    url(r'^addexpenseDec/', views.addexpenseDec),
    url(r'^deleteexpense/<int:id>/', views.delete),
    url(r'^options/', views.options),
    url(r'^login/', LoginView.as_view()),
    url(r'^customreg/', views.customreg),
    url(r'^check/', views.check),
    url(r'^logoutview/', views.logoutview)
]
