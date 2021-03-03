from django.urls import path
from .import views

urlpatterns = [
    # path('',views.home, name='home'),
    # path('add',views.add, name='add')
    path('', views.home, name='home'),
    path('result',views.result, name="result")
    
    # path('time',views.time, name='time')
]