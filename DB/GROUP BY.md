# 여러가지 함수

### 문자열
- SUBSTR 문자열 가르기
- TRIM LTRIM RTRIM 문자열 공백제거
- LENGTH 문자열 길이
- REPLACE 패턴에 일치하는 부분을 변경
- UPPER LOWER 대소문자 변경
- || 문자열 합치기

### 숫자함수
- ABS 절대 값
- SIGN 부호(양수 ,음수,0)
- MOD(1,2) 숫자 1을 2로 나눈 나머지
- CEIL , FLOOR ROUND 올림 내림 반올림
- POWER(1,2) 1의 2제곱
- SQRT 제곱근

### GROUP BY
- 행 집합에서 요약 행 집합을 만듦
- 선택된 행 그룹을 하나 이상의 열값으로 요약행으로 만듦
- 문장에 WHERE이 포함된 경우 WHERE절 뒤에 작성해야함
- GROUP BY절에 명시하지 않은 컬럼은 별도로 지정할 수 없음
- GROUP BY의 결과는 정렬되지 않음

### HAVING 
- 집계함수는 WHERE 절의 조건식에서는 사용할 수 없음(실행 순서에 의해)
- WHERE로 처리하는 것이 앞에 있기때문
- WHERE 대신 HAVING을 사용


### SELECT 문장 실행 순서
1. FROM => WHERE => GROUP BY => HAVING => SELECT => ORDER BY
2. FROM 테이블을 대상으로
3.  WHRE 제약조건에 맞춰서 뽑아서
4. GROUP BY 그룹화한다.
5. HAVING 그룹 중에 조건과 맞는 것 만을
6. SELECT 조회하여
7. ORDER BY 정렬하고
8. LIMIT/OFFSET 특정 위치의 값을 가져온다.


#### ALTER TABLE
- 테이블 이름 변경 
- 새로운 컬럼 추가
- 컬럼 이름 수정
- 컬럼 삭제