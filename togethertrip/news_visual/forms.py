from django import forms
from crawling.models import naver_news

# 질문글 등록 처리용 폼 클래스 : 모델과 바로 연결되는 ModelForm임
class NaverNewsForm(forms.ModelForm):  # 폼 종류 지정 상속
    class Meta:
        model = naver_news  # 사용할 모델 지정
        fields = ['NEWS_TITLE', 'NEWS_URL']  # 사용할 모델 속성 지정
        labels = {
            'NEWS_TITLE': '제목',
            'NEWS_URL': 'url',
        }
