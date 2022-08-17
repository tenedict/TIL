-- SQLite
create table users(
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL,
        city TEXT NOT NULL,
        phone TEXT NOT NULL,
        balance INTEGER NOT NULL
        );
.mode csv
.import users.csv users

SELECT * FROM users WHERE age >= 30;

SELECT first_name FROM users WHERE age >= 30;

SELECT first_name FROM users WHERE last_name = '문';

SELECT last_name FROM users WHERE first_name = '선영';

SELECT COUNT(*) FROM users WHERE age = 23;

SELECT MAX(balance), first_name FROM users WHERE last_name = '문';

SELECT avg(balance), first_name FROM users WHERE last_name = '문';



