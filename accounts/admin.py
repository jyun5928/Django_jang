# 필요한 기능 import
from django.contrib import admin
from .models import CustomUser

#CustomUser 모델 등록
admin.site.register(CustomUser)
