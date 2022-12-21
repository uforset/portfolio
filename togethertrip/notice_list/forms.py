from django import forms
from notice_list.models import Notice_list
# # from .models import
# from dataclasses import field
#
class Notice_listForm(forms.ModelForm):
    class Meta:
        model = Notice_list
        fields = ['NOTICE_TITLE', 'NOTICE_CONTENT']
        label = {
            'NOTICE_TITLE':'제목',
            'NOTICE_CONTENT':'내용',
        }