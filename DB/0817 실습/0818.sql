SELECT * FROM users LIMIT 1;

SELECT 
    last_name || first_name 이름,
    age,
    city,
    phone,
    balance
FROM users
LIMIT 5;

-- || 이거 쓰면 문자열 합쳐짐

SELECT 
    LENGTH(first_name),
    first_name
FROM users
LIMIT 5;

-- lenght 쓰면 글자 길이 나타남

SELECT 
    first_name,
    phone,
    REPLACE(phone, '-', '')
FROM users
LIMIT 5;

-- replace 쓰면 파이썬처럼 바꾸기 쌉가능

SELECT MOD(5, 1)
FROM users
limit 2
-- 파이썬의 %임

SELECT CEIL(3.14), FLOOR(3.14), ROUND(3.14)
FROM users
LIMIT 1;
-- 올림 내림 반올림이다.

SELECT SQRT(9)
FROM users
LIMIT 1;
-- 9의 제곱근이다.

SELECT POWER(9, 2)
FROM users
LIMIT 1;
-- 제곱 쌉가능