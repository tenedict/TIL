SELECT last_name,first_name,age
FROM users
WHERE age = (SELECT min(age) 
FROM users
GROUP BY last_name)
GROUP by last_name;


SELECT min(age),last_name
FROM users
GROUP BY last_name;


SELECT first_name, age,last_name 
FROM users
WHERE age = (SELECT MIN(age) FROM users GROUP BY first_name);

-- 가장 나이가 적은 사람의 수
SELECT age, COUNT(*)
FROM users
GROUP BY age
ORDER BY age
LIMIT 1;



SELECT last_name,COUNT(*)
FROM users 
WHERE age = (SELECT MIN(age) FROM users);


SELECT AVG(balance) FROM users;

SELECT COUNT(*)
FROM users
WHERE balance > (SELECT AVG(balance) FROM users);

SELECT city
FROM users
WHERE last_name = '유' AND first_name = '은정';

SELECT 
    COUNT(*)
FROM users
WHERE city = (SELECT city FROM users
WHERE last_name = '유' AND first_name = '은정');


SELECT COUNT(*), AVG(balance), AVG(age)
FROM users;

SELECT 
    (SELECT COUNT(*) FROM users) AS 총인원,
    (SELECT AVG(balance) FROM users) AS 평균연봉;


SELECT 
    city
FROM users
WHERE last_name = '이' AND first_name = '은정';

SELECT 
    COUNT(*)
FROM users
WHERE city = (SELECT city FROM users
WHERE last_name = '이' AND first_name = '은정');


SELECT 
    COUNT(*)
FROM users
WHERE city IN (SELECT city FROM users
WHERE last_name = '이' AND first_name = '은정');

SELECT 
    COUNT(*)
FROM users
WHERE city IN (SELECT city FROM users
WHERE last_name = '이' AND first_name = '은정');

SELECT 
last_name,min(age)
FROM users
GROUP BY last_name;

SELECT last_name, age
FROM users
WHERE (last_name, age) in (SELECT 
last_name,min(age)
FROM users
GROUP BY last_name);