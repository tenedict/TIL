# Django Auth

- Django authentication system은 인증과 권한부여를 함께 제공함
    - 유저
    - 권한 및 그룹
    - 암호 해시 시스템
    - 폼 및 뷰 도구
    - 기타
- 필수 구성은 settings.py 의 INSTALLED_APPS에서 확인 가능
    - django.contrib.auth


첫번째!
    - accounts app생성
    - auth와 관련한 경로나 키워드들을 Django 내부적으로 accounts라는 이름으로 사용하고 있기 때문에 되도록 accounts로 지정하는 것을 권장
        - 다른 이름으로 설정해도 되지만 나중에 추가 설정을 해야 할 일들이 생기게 됨
    - url 분리
    - settings.py에 (AUTH_USER_MODEL = 'accounts.User')추가
       
두번째!
``` python
모델
    from django.contrib.auth.models import AbstractUser
        class User(AbstractUser):
            pass
```
모델
    from django.contrib.auth.models import AbstractUser
        class User(AbstractUser):
            pass
    
세번째!
```python
어드민
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
admin.site.register(User, UserAdmin)
```
네번째!
```python
# 유저생성
user = User.objects.create_user('john‘, ‘john@google.com’, ‘1q2w3e4r!’)
                                
# 비밀번호 변경
user = User.objects.get(pk=2)
User.set_password(‘new password’)
User.save()

# 인증
from django.contrib.auth import authenticate
user = authenticate(username='john', password='secret')                           
```
