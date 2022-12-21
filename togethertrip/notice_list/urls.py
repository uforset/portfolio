from django.urls import path
from . import views

app_name = 'notice_list'

urlpatterns = [
    path('',views.notice_page, name='notice_page'),
    path('notice_page',views.notice_page, name='notice_page'),
    path('<int:notice_list_id>/', views.notice_detail, name='notice_detail'),

    # 관리자용 공지등록, 공지수정
    path('notice_input',views.notice_input,name='notice_input'),
    # path('notice_list/modify/<int:notice_list_id>/notice_input', views.notice_list_modify, name='notice_list_modify'),
    path('<int:notice_list_id>/delete/', views.notice_list_delete, name='notice_delete'),#삭제 수정
    path('edit/<int:notice_list_id>/',views.notice_edit,name='notice_edit'),
]