# 필요한 기능 import
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# 필드 정의
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 게시물 제목 반환
    def __str__(self):
        return self.title