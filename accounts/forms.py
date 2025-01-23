# 필요한 기능 import
from django import forms
from .models import CustomUser 

# 사용자 가입을 위한 form 정의하는 클래스
class SignUpForm(forms.ModelForm):
    # 비밀번호 확인 필드
    password_confirmation = forms.CharField(widget=forms.PasswordInput)
    # 저장 메서드
    def save(self, commit=True):
        # save() 메서드를 호출해서 사용자 객체 생성
        user = super().save(commit=False)
        # 비밀번호를 안전하게 해시화하여 설정
        user.set_password(self.cleaned_data["password"])
        # commit이 True일 경우 저장
        if commit:
            user.save()
         # 저장된 사용자 객체 반환
        return user
    
    # 폼 메타 설정
    class Meta:
        model = CustomUser
        # 모델에서 사용할 필드
        fields = ['username', 'email', 'password', 'profile_image', 'bio'] 
    password = forms.CharField(widget=forms.PasswordInput)  # 비밀번호 필드를 정의
    password_confirmation = forms.CharField(widget=forms.PasswordInput)  # 비밀번호 확인

    # 비밀번호 확인 검사
    def clean_password_confirmation(self):
        # 비교 
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        # 비교한 비밀번호가 불일치하면 ValidationError 발생
        if password != password_confirmation:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")
         # 일치하면 비밀번호 확인 값을 반환
        return password_confirmation