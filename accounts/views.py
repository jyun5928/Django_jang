# 필요한 기능 import
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# 사용자 가입
def signup(request):
    # POST일 때
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES) # SignUpForm 객체 생성
        if form.is_valid(): # 폼 검사
            user = form.save() # 사용자 생성
            login(request, user)  # 로그인
            return redirect('accounts:login')  # 로그인 후 'login' 페이지로 리디렉션 
    else:
        form = SignUpForm()
    # 'user/signup.html' 템플릿에 폼을 전달해 렌더링
    return render(request, 'user/signup.html', {'form': form})


# 로그인
def login_view(request):
    # POST일 때 
    if request.method == 'POST':
        # 사용자가 입력한 username과 password를 가져옴
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 사용자 인증
        user = authenticate(request, username=username, password=password)
        print(f"Authenticated user: {user}")  
        # 인증된 사용자가 있을 경우
        if user is not None:
            # 로그인 처리
            login(request, user)
            # 로그인 후 사용자 프로필 페이지로 리디렉션
            return redirect('accounts:user_profile')  
        else:
            # 인증 실패 시 오류 메시지
            messages.error(request, "Invalid username or password.")
            return render(request, 'user/login.html')  
    return render(request, 'user/login.html')  


# 로그아웃
def logout_view(request):
    logout(request) # 현재 세션에서 로그아웃 처리
    return redirect('accounts:login')  # 로그아웃 후 로그인 페이지로 리디렉션


# 로그인된 사용자만 접근할 수 있는 프로필 페이지
@login_required  
def user_profile(request): # 현재 로그인된 사용자 정보를 가져옴
    user = request.user
    # 'user/profile.html' 템플릿에 사용자 정보를 전달하여 렌더링
    return render(request, 'user/profile.html', {'user': user})