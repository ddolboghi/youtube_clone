# youtube_clone
유튜브 클론 코딩

# main 앱
- youtube 첫 화면 구성

# to_do 앱
- 디자인 수정 with bootstrap

# 회원가입 구현
1. django-allauth 라이브러리 설치
2. settings.py > 
    INSTALLED_APPS = [
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    ]
    ...
    AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    )

    SITE_ID = 1

    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_EMAIL_VERIFICATION = 'none'

3. 프로젝트 폴더 urls.py > path('accounts/', include('allauth.urls')),
4. python manage.py migrate

# 개선사항
- done날짜 모델에 추가 및 done_list 페이지에 done날짜 표시
- Done List 버튼이 done_list 페이지에서 To Do List 버튼으로 바뀌고 누르면 todo_list 페이지로 넘어가도록 
  --> log in, log out 버튼 참고