# Template inheritance

    - 템플릿을 상속 받을 수 있음
   ```html
<!-- articles/templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- bootstrap CDN 작성 -->
<title>Document</title>
</head>
<body>
{% block content %}
{% endblock content %}
<!-- bootstrap CDN 작성 -->
</body>
</html>
```
```html
{% extends 'base.html' %}
{% block content %}
<h1>만나서 반가워요!!</h1>
<a href="/greeting/">greeting</a>
<a href="/dinner/">dinner</a>
{% endblock content %}
```

- 만약 템플릿 경로가 같은 템플릿 디렉토리가 아니라면
```html
# settings.py
TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [BASE_DIR / 'templates',],
'APP_DIRS': True,
'OPTIONS': {
'context_processors': [
'django.template.context_processors.debug',
'django.template.context_processors.request',
'django.contrib.auth.context_processors.auth',
'django.contrib.messages.context_processors.messages',
],
},
},
```