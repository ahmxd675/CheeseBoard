from django.urls import path
from CheeseBoardSite import views

app_name = 'CheeseBoardSite'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    # add this url to a button to logout
    path('logout/', views.logout, name='logout'),
]
