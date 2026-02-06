# Portfolio Task - Cinema System
You are working with a small database used by a cinema booking system.

The database contains the following tables:

customers(**customer_id**, customer_name)
films(**film_id**, title, age_rating)
screenings(**screening_id**, film_id, screen)
tickets(**ticket_id**, screening_id, customer_id, price)

You are provided with a Python file called `cinema.py` containing function stubs.
You should complete the functions as described below.


You can test your functions by running `test.py`.

## customer_tickets(conn, customer_id)


Write a function that returns details of tickets purchased by a specific customer.

The function should return a list of tuples containing (in order):
- the film title
- the screen
- the ticket price

Results should be ordered alphabetically by film title.

## screening_sales(conn)

Write a function that returns the number of tickets sold for each screening.

The function should return a list of tuples containing (in order):
- the screening ID
- the film title
- the number of tickets sold

All screenings should be included, even if no tickets were sold for that screening.

Results should be ordered by the number of tickets sold, from highest to lowest.


---


## top_customers_by_spend(conn, limit)

Write a function that returns the customers who have spent the most money on tickets.

The function should return a list of tuples containing (in order):
- the customer name
- the total amount spent on tickets


Only customers who have purchased at least one ticket should be included.

Results should be ordered by total amount spent, from highest to lowest, and limited to a specified number of rows (passed in by the argument `limit`)

---

## Submission notes

- Do not print from your functions - they need to return.
- Each function should return the data requested in the order specified.
- Do not change the function names or parameters.

You should submit cinema.py to the autograder.