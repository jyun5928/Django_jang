# 필요한 기능 import
from django.apps import AppConfig

# 'Accounts' 정의하는 클래스
class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    # 앱 이름 설정
    name = "accounts"
