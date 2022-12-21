from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
import datetime
from crawling.models import naver_news,COUNTRY
from .forms import NaverNewsForm
from html import unescape

def visual_detail(request):
    keyword = request.GET.get('keyword', '')
    c = COUNTRY.objects.filter(COUNTRY_NAME=keyword)
    if len(c)==0:
        news = ''
    else:
        news = naver_news.objects.filter(NEWS_TITLE__contains=keyword)
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    context = {'news': news, 'keyword': keyword, 'link': now}
    return render(request, 'naver/show.html', context)


def search_page(request):
    form = NaverNewsForm()
    context = {'news': form, }
    return render(request, 'naver/search.html', context)