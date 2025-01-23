# 필요한 기능 import
from django.contrib.auth.models import AbstractUser
from django.db import models

# AbstractUser 클래스를 상속받아 커스텀 사용자 모델 정의
class CustomUser(AbstractUser):
    # 프로필 사진 저장할 필드 정의
    # 'profile_images/' 디렉토리에 업로드, 기본값은 빈 값으로 설정
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    # 자기소개 저장할 텍스트 필드 정의
    # bio는 빈 값도 허용, 기본값은 null
    bio = models.TextField(blank=True, null=True)

    # 사용자의 이름을 반환하는 문자열 메서드 정의
    # 사용자 객체를 문자열로 출력할 때 'username'을 반환하도록 설정
    def __str__(self):
        return self.username