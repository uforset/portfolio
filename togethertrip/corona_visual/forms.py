from django import forms
from crawling.models import corona_info,trip_info


class CoronaInfoForm(forms.ModelForm):  # 폼 종류 지정 상속
    class Meta:
        model = corona_info  # 사용할 모델 지정
        fields = ['COUNTRY_NAME', 'ALL_CONFIRMED_CASES','DEAD_PERSON','FATALITY_RATE']  # 사용할 모델 속성 지정
        labels = {
            'COUNTRY_NAME': '국가명',
            'ALL_CONFIRMED_CASES': '전체확진자',
            'DEAD_PERSON':'전체사망자',
            'FATALITY_RATE':'치명률',
        }
