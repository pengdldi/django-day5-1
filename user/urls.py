from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
        path('register', views.register, name='register'),
        path('ttt/', views.ttt, name='ttt'),
        path('<int:question_id>/', views.detail, name='detail'),
        path('main/', views.main, name='main'),
        path('login/', views.login, name='login')
]

