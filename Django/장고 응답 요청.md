## 장고 실행
    1.가상환경 on
            1.  **가상환경** 생성: python -m **venv 가상환경**이름
            2.  가상환경 활성화: source **가상환경**이름/Scripts/activate.
            3.  **가상환경** 비활성화: deactivate
            4. pip install django==3.1.13
            5. pip freeze > requirements.txt
            6. 프로젝트 생성: django-admin startproject '플젝이름' .
            7. python manage.py runserver
            8. 어플리케이션 생성: python manage.py startapp articles(어플이름 복수 권장)

   ## 애플리케이션 구조
       - admin.py
           - 관리자용 페이지 설정
       - apps.py
           - 앱의 정보가 작성된 곳
           - 별도로 추가 코드를 작성하지 않음
       - models.py
           - 어플리케이션 사용하는 모델을 정의하는 곳
       - tests.py
           - 프로젝트 테스트 코드를 작성하는 곳
       - views.py
           - view함수들이 정의되는 곳
           - def index(request): return render(request, 'index.html')
       - 프로젝트 앱을 사용하려면 세팅.py에서 앱깔려있다는 리스트에 추가 해줘야함 (젤위에로 계속 적음)
 ## 요청과 응답
     URL > VIEW > TEMPLATE
     
1. url
      
```python
from django.urls import path
        from articles import views
        urlpatterns = [
        path('admin/', admin.site.urls),
        path('index/', views.index),
        ] 
```
2. views
```python
def index(request):
    return render(request, template_name, context)
```
- rende()
    - 주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 렌더링 된 텍스트와 함께 응답 객체를 반환하는 함수
- templates
    - 실제 내용을 보여주는데 사용되는 파일
    - 파일의 구조나 레이아웃을 정의
    - Template 파일의 기본 경로
    - 