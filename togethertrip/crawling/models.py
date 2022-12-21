from django.db import models

class naver_news(models.Model):
    NEWS_TITLE = models.CharField(max_length=150)               #뉴스 타이틀
    NEWS_URL = models.URLField(unique=True)                     #뉴스 url


    def __str__(self):
        return self.NEWS_TITLE


class COUNTRY(models.Model):
    COUNTRY_NAME = models.CharField(unique=True,max_length=150) #국가명
    KEYWORD_COUNT = models.IntegerField(default=0)              #뉴스 키워드 카운트


    def __str__(self):
        return self.COUNTRY_NAME


class corona_info(models.Model):
    COUNTRY_NAME = models.CharField(max_length=30)              # 국가명
    ALL_CONFIRMED_CASES = models.IntegerField()                 # 전체 확진자
    DEAD_PERSON = models.IntegerField()                         # 전체 사망자
    FATALITY_RATE = models.FloatField()                         # 치명률



class trip_info(models.Model):
    TRAVEL_WARNING = models.CharField(max_length=300)           #여행 제한
    QUARANTINE = models.CharField(max_length=300)               #격리 조치 관련 지침
    VACCINE = models.CharField(max_length=300)                  #백신 예방접종
    CORONA_TEST = models.CharField(max_length=300)              #코로나19진단검사
    DOCUMENT_VISA = models.CharField(max_length=300)            #서류 및 비자
    TRAVEL_INSURANCE = models.CharField(max_length=300)         #여행/의료 보험
    MASK = models.CharField(max_length=300)                     #마스크
    COUNTRY_NAME = models.CharField(max_length=30)              #국가명

    def __str__(self):
        return self.COUNTRY_NAME