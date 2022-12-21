from django.shortcuts import render
from .models import COUNTRY, naver_news, corona_info, trip_info
from django.http import HttpResponse
from konlpy.tag import Okt
# Create your views here.
def country_setting(request):
    __url = {'인도': 'india', '터키': 'turkey', '레바논': 'lebanon', '몰디브': 'maldives', '바레인': 'bahrain',
             '방글라데시': 'bangladesh', '스리랑카': 'sri-lanka', '우즈베키스탄': 'uzbekistan', '이라크': 'iraq', '이란': 'iran',
             '중국': 'china', '카타르': 'qatar', '캄보디아': 'cambodia', '파키스탄': 'pakistan',
             '시리아': 'syria', '네팔': 'nepal', '대만': 'taiwan', '라오스': 'laos', '말레이시아': 'malaysia',
             '몽골': 'mongolia', '미얀마': 'myanmar', '베트남': 'vietnam', '사우디아라비아': 'saudi-arabia',
             '싱가포르': 'singapore', '아제르바이잔': 'azerbaijan', '이스라엘': 'israel', '인도네시아': 'indonesia', '일본': 'japan',
             '카자흐스탄': 'kazakhstan', '태국': 'thailand', '필리핀': 'philippines',
             '브라질': 'brazil', '콜롬비아': 'colombia', '파라과이': 'paraguay', '페루': 'peru', '베네수엘라': 'venezuela',
             '아르헨티나': 'argentina', '우루과이': 'uruguay', '칠레': 'chile', '네덜란드': 'netherlands', '노르웨이': 'norway',
             '덴마크': 'denmark', '독일': 'germany', '러시아': 'russia', '불가리아': 'bulgaria', '스위스': 'switzerland',
             '스페인': 'spain',
             '아이슬란드': 'iceland', '아일랜드': 'ireland', '영국': 'united-kingdom', '포르투갈': 'portugal', '프랑스': 'france',
             '그리스': 'greece',
             '리투아니아': 'lithuania', '벨기에': 'belgium', '벨라루스': 'belarus', '체코': 'czech-republic', '스웨덴': 'sweden',
             '에스토니아': 'estonia', '핀란드': 'finland',
             '슬로베니아': 'slovenia', '라트비아': 'latvia', '우크라이나': 'ukraine', '이탈리아': 'italy', '조지아': 'georgia',
             '크로아티아': 'croatia', '폴란드': 'poland',
             '헝가리': 'hungary', '루마니아': 'romania', '그린란드': 'greenland', '오스트리아': 'austria', '멕시코': 'mexico',
             '엘살바도르': 'el-salvador', '과테말라': 'guatemala', '아이티': 'haiti', '자메이카': 'jamaica', '쿠바': 'cuba',
             '파나마': 'panama',
             '미국': 'united-states', '캐나다': 'canada', '뉴질랜드': 'new-zealand', '사모아': 'samoa', '호주': 'australia',
             '가나': 'ghana',
             '르완다': 'rwanda', '모로코': 'morocco', '알제리': 'algeria', '에티오피아': 'ethiopia', '이집트': 'egypt',
             '잠비아': 'zambia', '중앙아프리카공화국': 'central-african-republic', '차드': 'chad',
             '케냐': 'kenya', '탄자니아': 'tanzania', '나이지리아': 'nigeria', '남아프리카공화국': 'south-africa', '짐바브웨': 'zimbabwe',
             '리비아': 'libya', '세네갈': 'senegal',
             '우간다': 'uganda', }

    print(__url)
    co = list(__url.keys())
    for name in co:
        COUNTRY(COUNTRY_NAME=name).save()
    return HttpResponse('생성성공')
