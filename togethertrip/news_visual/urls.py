from django.urls import path
from . import views

app_name = 'news_visual'
urlpatterns = [
    path('visualdetail/', views.visual_detail, name= 'visual_detail'),
    path('search/',views.search_page,name='search'),
]
