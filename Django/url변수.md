# Variable routing
      - url 주소를 변수로 사용하는 것을 의미
      - url의 일부를 변수로 지정하여 view함수의 인자로 넘길 수 있음
      - 변수는 <>로 정의 
 ```python
urlpatterns = [
...,
# path('hello/<str:name>/', views.hello),
path('hello/<name>/', views.hello),
]
```
```python
def hello(request, name):
context = {
'name': name,
}
return render(request, 'hello.html', context)
```
