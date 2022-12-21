from django.http import HttpResponse
from .forms import Notice_listForm
from django.db.models import Q
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Notice_list
from django.core.paginator import Paginator

# 공지사항 리스트와 페이지 처리
def notice_page(request):
    page = request.GET.get('page','1') #페이지
    kw = request.GET.get('kw', '') #검색어
    notice_list = Notice_list.objects.order_by('-id')
    if kw:
        notice_list = notice_list.filter(
            Q(NOTICE_TITLE__icontains=kw) | #제목 검색
            Q(NOTICE_CONTENT__icontains=kw) #내용검색
        ).distinct()
    paginator = Paginator(notice_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'notice_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'notice_list/notice_title.html', context)

# 공지사항 상세보기
def notice_detail(request, notice_list_id):
    # notice_list = Notice_list.objects.get(notice_list_id)
    if request.method=='POST':
        form = Notice_listForm()
        context = {'form':form}
        return render(request, 'notice_list/notice_edit.html', context)
    else:
        notice_list = get_object_or_404(Notice_list, pk=notice_list_id)
        default_READCOUNT = notice_list.READCOUNT
        notice_list.READCOUNT = default_READCOUNT + 1
        notice_list.save()
        context = {'notice_list': notice_list,}
    return render(request, 'notice_list/notice_detail.html', context)

# 관리자용 공지사항 등록
def notice_input(request):
    if request.method == 'POST':
        form = Notice_listForm(request.POST)
        if form.is_valid():
            notice_list = form.save(commit=False)
            notice_list.NOTICE_AUTHOR = request.user # 속성에 로그인 계정 저장
            notice_list.NOTICE_DATE=timezone.now()
            notice_list.save()
            return redirect('notice_list:notice_page')
    else:
        form = Notice_listForm()
    context = {'form': form}
    return render(request, 'notice_list/notice_input.html', context)


def notice_list_delete(request, notice_list_id):    #삭제 수정
    del_board = Notice_list.objects.get(pk=notice_list_id)
    del_board.delete()
    return redirect('notice_list:notice_page')


#공지사항 수정
def notice_edit(request, notice_list_id):
    if request.method=="POST":
        notice = Notice_list.objects.get(pk=notice_list_id)
        notice.NOTICE_TITLE = request.POST["NOTICE_TITLE"]
        notice.NOTICE_CONTENT = request.POST["NOTICE_CONTENT"]
        notice.save()
        return redirect('notice_list:notice_page')
    else:
        form = Notice_listForm
        return render(request,'notice_list/notice_edit.html',{'form':form})

# 관리자용 수정
# @login_required(login_url='common:login') #수정
# def notice_list_modify(request, notice_list_id):
#     notice_list = get_object_or_404(Notice_list, pk=notice_list_id)
#     if request.user != notice_list.author:
#         messages.error(request, '수정권한이 없습니다')
#         return redirect('notice_list:notice_detail', notice_list_id=notice_list.id)
#     if request.method == "POST":
#         form = Notice_listForm(request.POST, instance=notice_list)
#         if form.is_valid():
#             notice_list = form.save(commit=False)
#             notice_list.modify_date = timezone.now()  # 수정일시 저장
#             notice_list.save()
#             return redirect('notice_list:notice_detail', notice_list_id=notice_list.id)
#     else:
#         form = Notice_listForm(instance=notice_list)
#     context = {'form': form}
#     return render(request, 'notice_list/notice_input.html', context)


# 관리자용 삭제
# @login_required(login_url='common:login') #수정
# def notice_list_delete(request, notice_list_id):
#     notice_list = get_object_or_404(Notice_list, pk=notice_list_id)
#     if request.user != notice_list.author:
#         messages.error(request, '삭제권한이 없습니다')
#     else:
#         notice_list.delete()
#     return redirect('notice_list:notice_list_detail', notice_list_id=notice_list.notice_list.id)

# 관리자용 공지사항 수정
# def notice_edit(request):
#     if request.method == 'POST':
#         form = Notice_listForm(request.POST)
#         if form.is_valid():
#             notice_list = form.save(commit=False)
#             notice_list.NOTICE_DATE=timezone.now()
#             notice_list.save()
#             return redirect('notice_list:notice_title')
#     else:
#         form = Notice_listForm()
#     context = {'form': form}
#     return render(request, 'notice_list/notice_input.html', context )

