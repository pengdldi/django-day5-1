from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
        path('<str:cname1>/<str:cname2>/',views.novel,name='web_novel')
]
