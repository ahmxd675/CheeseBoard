from django.urls import path
from CheeseBoardSite import views
from django.contrib.auth.views import LogoutView

app_name = 'CheeseBoardSite'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    # add this url to a button to logout
    path('logout/', views.user_logout, name='logout'),
    path('search/', views.search, name='search'),
    path('account', views.account, name='account'),
]
