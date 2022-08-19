
SELECT smoking,count(*)
FROM healthcare
GROUP BY smoking;

SELECT is_drinking,count(*)
FROM healthcare
GROUP BY is_drinking;

SELECT is_drinking, count(is_drinking)
FROM healthcare
GROUP BY is_drinking
HAVING blood_pressure > 200;

SELECT sido, COUNT(sido)
FROM healthcare
GROUP BY sido
HAVING COUNT(sido) > 5000;

SELECT height,weight, count(height)
FROM healthcare
GROUP BY height,weight
ORDER BY count(HEIGHT) DESC
LIMIT 5;

SELECT is_drinking,AVG(waist)
FROM healthcare
GROUP BY is_drinking;

SELECT gender 성별, round(AVG(va_left),2) 평균윈쪽시력, round(AVG(va_right),2) 평균오른쪽시력
FROM healthcare
GROUP BY gender;

SELECT age 나이,avg(height) '평균 키',avg(weight)'평균 몸무게'
FROM healthcare
GROUP BY age
HAVING avg(height) >160 AND avg(weight) >60;

SELECT   is_drinking,smoking, (weight/((height*0.01)*(height*0.01))) BMI
FROM   healthcare
GROUP BY  is_drinking,smoking
Having is_drinking  and smoking;


