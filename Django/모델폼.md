# modelfrom

정의한 모델폼 클래스 안에 Meta클래스를 선언
어떤 모델을 기반으로 할 것인지에 대한 정보를 Meta클래스에 지정
```
from django import forms
from .models import Article
class ArticleForm(forms.ModelForm):
class Meta:
model = Article
fields = '__all_
```

라벨과 인풋 쌍

• as_p()
• 각 필드가 단락(<p> 태그)으로 감싸져서 렌더링
• as_ul()
• 각 필드가 목록 항목(<li> 태그)으로 감싸져서 렌더링
• <ul> 태그는 직접 작성해야 한다.
• as_table()
• 각 필드가 테이블(<tr> 태그) 행으로 감싸져서 렌더링