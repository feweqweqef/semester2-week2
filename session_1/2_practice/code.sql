-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit


-- write your sql code here
Show book title, member name, and loan date.
SELECT Books.title AS book_title, Members.name AS member_name, Loans.loan_date 
FROM Loans JOIN Books ON Loans.book_id = Books.id 
JOIN Members ON Loans.member_id = Members.id;

SELECT Books.title AS book_title, Loans.loan_date AS LoanDate 
FROM Books 
LEFT JOIN Loans ON Books.id = Loans.book_id;