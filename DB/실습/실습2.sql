-- SQLite
CREATE TABLE classmates (
    name TEXT,
    age INT,
    address TEXT
);


INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
SELECT * FROM classmates;
INSERT INTO classmates (name, age, address) VALUES ('홍길동', 23, '서울');
INSERT INTO classmates VALUES ('김철수', 40, '서울');