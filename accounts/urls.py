# 필요한 기능 import
from django.urls import path
from . import views

# 앱 정의
app_name = 'accounts'

# 사용하는 각각의 URL과 views 호출
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.user_profile, name='user_profile'),
]
