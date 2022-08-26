# ORM

   Object-Relational-Mapping
   - 객체 지향 프로그래밍 언어를 사용하여 혼환되지 않는 유형의 시스템 간의 데이터를 변환하는 프로그래밍 기술
   - 파이썬에서는 SQLAlchemy,peewee등 라이브러리가 있고
   장고프레임워크에서는 내장 장고 ORM을 사용
   
   - 객체로 DB를 조작한다.
   Genre.objects.all()
  모델 설계 및 반영
  클래쓰 생성 
  ```sql
class Genre(models.Model):
name = models.CharField(max_length=30)
```
클래스 내용으로 데이터베이스에 반영하기 위한 마이그레이션 파일을 생성한다.
```bash
$ python manage.py makemigrations
```
##  Migration
- 모델에 생긴 변화를 DB에 반영하기 위한 방법
- 마이그레이션 파일을 만들어 DB스키마를 반영한다.
- 명령어
    - makemigrations 마이그레이션 파일 생성
    - migrate 마이그레이션을 DB에 반영

## Create
```python
 1. create 메서드 활용
Genre.objects.create(name='발라드')
 2. 인스턴스 조작
genre = Genre()
genre.name = '인디밴드'
genre.save()
```

## Read
```python
1\. 전체 데이터 조회 
Genre.objects.all()
2\. 일부 데이터 조회(get)
Genre.objects.get(id=1)
3\. 일부 데이터 조회(filter)
Genre.objects.filter(id=1)
```

## Update
```python
1. genre 객체 활용
genre = Genre.objects.get(id=1)
2. genre 객체 속성 변경
genre.name = '트로트’
3. genre  객체저장
genre.save()
```

## Delete
```python 
1. genre 객체 활용
genre = Genre.objects.get(id=1) 
2. genre 객체 삭제
genre.delete()
```