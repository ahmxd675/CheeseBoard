from django.urls import path
from CheeseBoardSite import views
from django.urls import include

app_name = 'CheeseBoardSite'
urlpatterns = [
    path('', views.index, name='index'),

]
