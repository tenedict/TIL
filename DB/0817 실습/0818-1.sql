-- SQLite
SELECT last_name, COUNT(*)
FROM users
GROUP BY last_name;

-- 그룹바이에서 활용하는 칼럼 제외하고 집계함수 써야댐

SELECT last_name, AVG(age), COUNT(*)
FROM users
GROUP BY last_name;

SELECT last_name, age
FROM users
WHERE last_name = '곽';

-- 그룹바이는 결과가 정렬되지 않는다.

SELECT *
FROM users
LIMIT 5;

SELECT last_name, age
FROM users
GROUP BY age
ORDER BY age DESC
LIMIT 5;


SELECT last_name, COUNT(last_name)
FROM users
GROUP BY last_name
HAVING COUNT(last_name) < 20;