from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('gugu',views.gu),
    path('test/',views.test),
    path('test2/',views.test2),
    path('signup/',views.signup)
]
