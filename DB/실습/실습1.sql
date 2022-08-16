-- SQLite
CREATE TABLE classmates (
    id INTEGER PRIMARY KEY, 
    name TEXT
);
.tables

.schema classmates

INSERT INTO classmates VALUES (1, '챨리푸스');

--테이블 조회
SELECT * FROM classmates;

INSERT INTO classmates VALUES (2, '문재윤');

-- 테이블 삭제
DROP TABLE classmates;