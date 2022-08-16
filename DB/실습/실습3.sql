-- SQLite
CREATE TABLE classmates (
    name TEXT,
    age INT,
    address TEXT
);


INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
INSERT INTO classmates (name, age, address) VALUES ('문재윤', 23, '부산');
INSERT INTO classmates VALUES ('후종', 40, '제주');
SELECT * FROM classmates;

SELECT rorid, * FROM classmates;