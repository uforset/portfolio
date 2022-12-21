from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main_page(request):
    return render(request,'main_page.html')

def test_page(request):
    return HttpResponse("로그인")

