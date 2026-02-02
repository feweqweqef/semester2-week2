-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit


-- write your sql code here
-- **List all loans**  
-- Show book title, member name, and loan date.

SELECT Books.title AS book_title, Members.name AS member_name, Loans.loan_date 
FROM Loans JOIN Books ON Loans.book_id = Books.id 
JOIN Members ON Loans.member_id = Members.id;

-- **Books and loans**--  
-- List all books and any loans associated with them.--
SELECT Books.title AS book_title, Loans.loan_date AS LoanDate 
FROM Books 
LEFT JOIN Loans ON Books.id = Loans.book_id;

--**Branches and books**  --
-- List all library branches and the books they hold.--
SELECT LibraryBranch.name AS library_branch, 
Books.title AS book_title 
FROM LibraryBranch 
LEFT JOIN Books ON LibraryBranch.id = Books.id;

--**Branch book counts** -- 
-- Show each library branch and the number of books it holds.--
SELECT LibraryBranch.name AS library_branch, 
COUNT(Books.id) AS book_count 
FROM LibraryBranch 
LEFT JOIN Books ON LibraryBranch.id = Books.branch_id 
GROUP BY LibraryBranch.id;

--  **Branches with more than 7 books**  --
-- Show branches that hold more than 7 books.--
SELECT LibraryBranch.name AS library_branch, 
COUNT(Books.id) AS book_count
FROM LibraryBranch 
LEFT JOIN Books ON LibraryBranch.id = Books.branch_id
GROUP BY LibraryBranch.id
HAVING COUNT(Books.id) > 7;

--**Members and loans** -- 
-- List all members and the number of loans they have made. --
SELECT Members.name AS member_name, COUNT(Loans.id) AS loan_id
FROM Members 
LEFT JOIN Loans ON Members.id = Loans.member_id
GROUP BY Members.id;

-- **Members who never borrowed**  
-- Identify members who have never borrowed a book. --
SELECT Members.name AS member_name FROM Members
LEFT JOIN Loans ON Members.id = Loans.member_id
GROUP BY Members.id
HAVING COUNT(Loans.id) = 0;

-- **Branch loan totals** -- 
-- For each library branch, show the total number of loans for books in that branch. --
SELECT LibraryBranch.name AS library_branch, COUNT(Loans.id) AS total_loans
FROM LibraryBranch 
LEFT JOIN Books ON LibraryBranch.id = Books.branch_id
LEFT JOIN Loans ON Books.id = Loans.book_id
GROUP BY LibraryBranch.id;


--*Members with active loans** -- 
-- List members who currently have at least one active loan.--
SELECT DISTINCT
Members.name
FROM Members
JOIN Loans ON Members.id = Loans.member_id
WHERE Loans.return_date IS NULL;