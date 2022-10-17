# ✅장고 게시판 이미지 업로드
> 이번 파트에서는 장고로 게시글을 만들때 이미지를 업로드 하는 것을 배웠다.

## 미디어 파일
    - 사용자가 웹에서 업로드하는 정적 파일
    - 유저가 업로드하는 모든 정적 파일

###  미디어관련필드
    - ImageField
        - 이미지 업로드에 사용하는 필드
        - 사요하려면 Pillow라이브러리 필수

    - FileField
        - 파일 업로드에 사용되는 필드
        - 2개의 선택인자를 가지고 있다
            - upload_to
            - storage
           
           
## 이미지 받아오기

   1. settings.py에 MEDIA_ROOT, MEDIA_URL설정
       - 여기서 ROOT는 미디어 파일을 저장할 절대 경로이다.
       - URL은 업로드 된 파일의 주소를 만들어주는 역할이다.
   2. urls.py에서 설정해준다.
       ```python
        \+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
      ```
  3. 모델을 설정해준다.
          - ImageField에서 `upload_to=‘images/’` (실제 이미지가 저장되는 경로를 지정해준다.)
          - blank = True를 활용해  ImageField에 빈 문자열이 허용되도록 설정
          - ※ 장고에서는 NULL이 아닌 빈 문자열을 사용하는 것을 규칙으로 한다.

   4. html작성 
           - form enctype을 지정해준다.
           -  `enctype="multipart/form-data"`
           -   인코딩 기본값은 모든 문자 인코딩(application/x-www-form-urlencoded)이다.
           -   인코딩을 하지않은 문자상태를 원하면 'text/plain'이다.
    5. views 설정
           - create함수에서 request.FILES 객체로 전달된다.
     
## 이미지 업로드

   1. img태그 활용
         - article.image.url == 업로드 파일의 경로
         - article.image == 업로드 파일의 파일 이름
   
## 이미지 수정하기

   1. 받아오는 것과 같다.
       - 덮어쓰는 방식이다.



## 이미지 Resizing

- 실제 원본이미지를 서버에 그대로 업로드 하는 것은 서버의 부담이 큰 작업이다.
- django-imagekit 라이브러리를 활용한다.

1. pip install django-imagekit
2. INSTALLED_APPS에 'imagekit'추가
3. 모델에서 `ProcessedImageField()`를 사용한다.
    - 파라미터로 작성된 값들은 변경이 되더라도 다시 makemigrations해줄필요없이 즉시 반영된다.
   ```python
class   Article(models.Model):

  title = models.CharField(max_length=20)

  content = models.TextField()

  created_at = models.DateTimeField(auto\_now\_add=True)

  updated_at = models.DateTimeField(auto_now=True)

  thumbnail = ProcessedImageField(upload_to='images/', blank=True,

  processors=\[ResizeToFill(1200, 960)\],

  format='JPEG',

  options={'quality': 80})

  image = models.ImageField(upload_to='images/', blank=True)
```
    