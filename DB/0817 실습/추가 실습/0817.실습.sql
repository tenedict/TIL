-- 테이블 만들기
CREATE TABLE healthcare (
id PRIMARY KEY,
sido INTEGER NOT NULL,
gender INTEGER NOT NULL,
age INTEGER NOT NULL,
height INTEGER NOT NULL,
weight INTEGER NOT NULL,
waist REAL NOT NULL,
va_left REAL NOT NULL,
va_right REAL NOT NULL,
blood_pressure INTEGER NOT NULL,
smoking INTEGER NOT NULL,
is_drinking BOOLEAN NOT NULL
);

-- csv import 하기
.mode csv 
.import health.csv healthcare

SELECT MAX(age),MIN(age) FROM healthcare ;

SELECT * FROM healthcare;

SELECT MAX(height),MIN(height),MAX(weight),MIN(weight) FROM healthcare ;

SELECT COUNT(*) FROM healthcare WHERE height>= 160 and height <= 170;

SELECT * FROM healthcare WHERE is_drinking  ORDER BY waist DESC LIMIT 5;

SELECT COUNT(*) FROM healthcare where va_left >= 1.5 and va_right >= 1.5 and is_drinking;

SELECT COUNT(*) FROM healthcare where blood_pressure <120;

SELECT AVG(waist) FROM healthcare where blood_pressure > 140;

SELECT AVG(height),AVG(weight) FROM healthcare where gender = 1;

SELECT id, height, weight FROM healthcare ORDER BY height DESC, weight DESC LIMIT 1 OFFSET 1;

SELECT count(*) FROM healthcare WHERE (weight/((height*0.01)*(height*0.01))) >= 30;

SELECT id,(weight/((height*0.01)*(height*0.01))) FROM healthcare WHERE smoking = 3 ORDER BY (weight/((height*0.01)*(height*0.01))) DESC LIMIT 5;

SELECT * FROM healthcare WHERE is_drinking AND NOT smoking = 0 ORDER BY weight DESC LIMIT 2;

SELECT count(*) FROM healthcare WHERE height < 184 and weight >70 and va_right <1 and va_left <1 and waist > 80;