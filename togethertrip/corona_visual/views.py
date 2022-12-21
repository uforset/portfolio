import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from crawling.models import corona_info, trip_info
from .forms import CoronaInfoForm


def visual_detail(request):
    keyword = request.GET.get('keyword', '')

    corona = corona_info.objects.get(COUNTRY_NAME__contains=keyword)
    trip = trip_info.objects.get(COUNTRY_NAME__contains=keyword)

    now = datetime.datetime.now().strftime("%Y-%m-%d")
    context = {'corona': corona, 'trip': trip, 'day': now}
    return render(request, 'corona/show.html', context)


def search_page(request):
    corona_form = CoronaInfoForm()
    # trip_form = TripInfoInfoForm()
    context = {'corona_form': corona_form}
    return render(request, 'corona/search.html', context)
