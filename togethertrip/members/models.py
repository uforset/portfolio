from django.db import models
from django.contrib.auth.models import AbstractUser

class MEMBERS(models.Model):
    USERNAME = models.CharField("이름",unique=True, max_length=40)
    BIRTHDATE = models.CharField("주민번호",unique=True, max_length=14)
    EMAIL = models.CharField("이메일",unique=True, max_length=25)
    PHONE = models.CharField("핸드폰번호",unique=True, max_length=13)
    USERPWD = models.CharField("비밀번호", max_length=20)
    STATUS = models.CharField("회원상태", max_length=20)
    ADDR = models.CharField("주소", max_length=200)

# 구글링
class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    university = models.CharField(max_length=50)
    location = models.CharField(max_length=200)