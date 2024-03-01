from django.urls import path
from CheeseBoardSite import views

app_name = 'CheeseBoardSite'
urlpatterns = [
    path('', views.index, name='index'),

]
