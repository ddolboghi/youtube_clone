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

# view --> js
- view의 값을 js로 넘겨주려면 템플릿 태그 사용하면 됌!

# issue
- html의 form 값을 모델 값으로 저장하는 방법 찾기