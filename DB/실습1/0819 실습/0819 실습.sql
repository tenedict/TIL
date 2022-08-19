--1
.tables
--2
--3
SELECT Title
FROM albums
ORDER BY title DESC
LIMIT 5;
--4
SELECT COUNT(*) '고객 수'
FROM customers;

SELECT firstname,lastname
FROM customers
WHERE country = 'USA'
ORDER BY firstname DESC
LIMIT 5;


SELECT *
FROM invoices
WHERE BillingPostalCode is NULL
ORDER BY InvoiceDate DESC
LIMIT 5;


SELECT count(*)
FROM invoices
WHERE strftime('%Y',invoicedate)= '2013';
--9
SELECT CustomerId 고객ID, FirstName 이름, LastName 성
FROM customers 
WHERE 이름 LIKE 'L%' ORDER BY 고객ID;
-- 10
SELECT country, count(*)
FROM customers
group by country;
--11
SELECT artistid,count(*) '앨범 수'
FROM albums
GROUP BY artistid	Rotenturmstraße 4, 1010 Innere Stadt	Vienne	NULL	Austria	1010	+43 01 5134505	NULL	astrid.gruber@apple.at	5
8	Daan	Peeters	NULL	Grétrystraat 63
ORDER BY count(*) DESC
LIMIT 1;
--12
SELECT ArtistId, COUNT(*) "앨범 수" 
FROM albums 
GROUP BY ArtistId 
HAVING "앨범 수" >= 10 
ORDER BY "앨범 수" DESC;

--13
SELECT COUNT(*) "고객 수", Country, State 
FROM customers 
WHERE State is NOT NULL 
GROUP BY Country, State 
ORDER BY "고객 수" DESC, Country DESC LIMIT 5;

--14
SELECT 
    CustomerId, Fax, 
    CASE 
        WHEN Fax is not NULL THEN 'O' 
        WHEN Fax is NULL THEN 'X' 
    END AS "Fax 유/무" 
FROM customers 
ORDER BY CustomerId LIMIT 5;

--15
SELECT
    LastName,
    FirstName,
    cast(strftime('%Y') AS INTEGER)-cast(strftime('%Y',BirthDate) AS INTEGER)+1 AS 나이
FROM employees
ORDER BY EmployeeId;

--16
SELECT
    Name
FROM artists
WHERE ArtistId = 
(SELECT ArtistId 
FROM albums 
GROUP BY ArtistId 
ORDER BY COUNT(*) DESC 
LIMIT 1);

-- 17
SELECT
    Name
FROM genres
WHERE GenreId = 
(SELECT GenreId
FROM tracks
GROUP BY GenreId ORDER BY COUNT(*) 
LIMIT 1);




