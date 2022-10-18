# ✅장고 1:N 관계
> 이번 파트에서는 포린키를 활용해 데이터를 테이블, 행, 열 등으로 나누어 구조화하는 방식중 1:N관게를 배웠다

## Foreign Key
- 외래키
- 관계형 데이터베이스에서 다른 테이블의 행을 식별할 수 있는 키
- 참조되는 테이블의 기본 키를 가리킴
- 참조하는 테이블 행 여러 개가, 참조되는 테이블의 동일한 행을 참조할 수 있음
- **참조 무결성**
    - 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성
- 외래키가 반드시 부모 테이블의 기본 키 일 필요는 없지만 유일한 값이어야 함

### Foreign Key arguments
- 외래 키가 참조하는 객체가 사라졌을때
- on_delete
    - CASCADE : 부모 객체가 삭제 됐을 때 이를 참조하는 객체도 삭제
    - PROTECT, SET_NULL등 다양한 옵션존재

### Foreing Key 정의
```
article = models.ForeignKey(Ariticle, on_delete=models.CASCADE)
```
- 소문자로 쓸것

### 관계모델 참조(Related manager)
- Related manager는 1:N 혹은 N:M 관게에서 사용 가능한 문맥
- **역참조**
    - 나를 참조하는 테이블을 참조하는 것
    - 게시글과 댓글이라면 게시글로 댓글을 참조가능
- django는 모델 간 1:N 혹은 N:M 관계가 설정되면 역참조할 때에 사용할 수 있는 manager를 생성
```python
article.comment_set.method()
```
 - comment_set이 기본 형태이다.
     - **모델명_set**형태로 만들어진다.
     - ForeignKey 모델에서 manager이름을 변경할 수 있다.
```python
article = models.ForeignKey(Ariticle, on_delete=models.CASCADE, related_name='comments')
```

### admin에 등록
- admin.py에서 import로 모델을 받아오고 **admin.site.register(모델명)** 을 작성해준다.



## create(댓글 구현)
```python
def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)
```
```html
<form action="{% url 'articles:comments_create' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
<input type="submit">
</form>
```
- forms.py에서 외래키 필드를 출력에서 제외한후 실행해야 별도로 외래키 필드를 입력받는 창이 뜨지 않는다.
- 외래키 데이터는 urls.py에서 해당게시글의 pk값을 받아와서 사용해햐한다.
- save(commit=False)
    - 아직 저장되지 않은 인스턴스를 반환한다.
    - 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용한다.
    - 인스턴스를 반환해서 저장하고 거기다가 다시 article값 넣어주고 진짜 저장을 시킨다.
```python
urlpatterns = [
...,
path('<int:pk>/comments/', views.comments_create,
name='comments_create'),
]
```

## read(댓글 목록)
```python
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
        }
    return render(request, 'articles/detail.html', context)
```
```html
{% for comment in comments %}
    <li>{{ comment.content }}</li>
{% endfor %}
```

## delete(댓글 삭제)
```python
urlpatterns = [
path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),]
```
```python
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```
```html
<form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
{% csrf_token %}
<input type="submit" value="DELETE">
</form>
```

## 댓글 개수
   - **DTL filter - length**을 사용한다 .
   ```html
{{ comments|length }}
{{ article.comment_set.all|length }}
```
   - **Queryset API - count()**을 사용한다.
   ```html
{{ comments.count }}
{{ article.comment_set.count }}
```
    - empty를 활용하여 없는 경우를 출력한다.
  ```html
{% empty %}
 <p>댓글이 없어요.</P>
```