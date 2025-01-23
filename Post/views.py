# 필요한 기능 import
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# 게시물 목록
class PostListView(ListView):
    # 사용할 모델을 Post로 지정
    model = Post
    # 사용할 템플릿 파일
    template_name = 'Post/post_list.html'
    # 객체 이름을 'posts'로 설정  
    context_object_name = 'posts'


# 게시물 상세 정보
class PostDetailView(DetailView):
    # 사용할 모델을 Post로 지정
    model = Post
    # 사용할 템플릿 파일
    template_name = 'post/post_detail.html'
    # 객체 이름을 'posts'로 설정  
    context_object_name = 'post'


# 게시물 작성 폼을 제공하고, 사용자가 폼을 제출하면 새로운 게시물을 생성하는 뷰
class PostCreateView(LoginRequiredMixin, CreateView):
    # 폼이 유효할 경우, 현재 로그인한 사용자를 'author' 필드에 자동으로 설정
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # 사용할 모델을 Post로 지정
    model = Post
    # 사용할 템플릿 파일
    template_name = 'post/post_form.html'
    # 폼에서 사용할 필드
    fields = ['title', 'content']
    # 게시물 생성 후 리디렉션할 URL을 지정
    success_url = reverse_lazy('post:post_list')  


# 게시물 정보 수정
class PostUpdateView(UpdateView):
    # 사용할 모델을 Post로 지정
    model = Post
    # 사용할 템플릿 파일
    template_name = 'post/post_form.html'
    # 폼에서 사용할 필드
    fields = ['title', 'content']
    # 게시물 수정 후 리디렉션할 URL을 지정
    success_url = reverse_lazy('post:post_list')  


# 게시물 삭제
class PostDeleteView(DeleteView):
    # 사용할 모델을 Post로 지정
    model = Post
    # 사용할 템플릿 파일
    template_name = 'post/post_confirm_delete.html'
    # 게시물 삭제 후 리디렉션할 URL을 지정
    success_url = reverse_lazy('post:post_list')  