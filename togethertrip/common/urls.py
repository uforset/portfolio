from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'common'

urlpatterns = [
    path('coronalogin/',
         auth_views.LoginView.as_view(
             template_name='common/coronalogin.html'),
         name='coronalogin'),
    path('naverlogin/',
         auth_views.LoginView.as_view(
             template_name='common/naverlogin.html'),
         name='naverlogin'),
    path('',views.main_page,name='main_page'),
    path('main_page',views.main_page,name='main_page'),
    path('test/',views.test_page,name='test_page'),
]
