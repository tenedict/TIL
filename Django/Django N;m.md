# ✅장고 N:M관계
> 이번 파트에서는 ForeignKey를 사용하는 1:N관계에 이어 N:M관계를 배웠다.
## N:M
- 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
- 양쪽 모두에서 1:N관계를 가짐

## 중개 모델
```python
class Reservation(models.Model):
doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```
- 테이블을 따로 만들어서 서로 ForeignKey로 연결하면 N:M이다.

## Django ManytoManyField 작성
```python
class Patient(models.Model):
# ManyToManyField 작성
doctors = models.ManyToManyField(Doctor)
name = models.TextField()
```
- 테이블을 따로 만들지 않아도 된다.
- 중개테이블을 자동으로 생성한다.

### view
- add 와 remove를 사용해서 바로 추가하고 삭제 할 수 있다.

### related_name
- 모델 뒤 적어주면 _set 없이 related_name으로 적어주면된다.