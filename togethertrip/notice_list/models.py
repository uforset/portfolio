from django.db import models

# Create your models here.
class Notice_list(models.Model): # 공지사항 리스트
    NOTICE_TITLE = models.CharField("제목",max_length=200) # 제목
    # NOTICE_UPFILE = models.FileField("첨부파일",upload_to='uploads/') #파일명
    NOTICE_WRITER = models.CharField("작성자",max_length=30) # 작성자
    NOTICE_DATE = models.DateTimeField("작성일",auto_now_add=True) # 작성일(등록날짜)
    READCOUNT = models.IntegerField("조회수",default=0) # 조회수
    NOTICE_CONTENT = models.TextField("공지내용", null=True)  # 내용

    def __str__(self):
        return self.NOTICE_TITLE