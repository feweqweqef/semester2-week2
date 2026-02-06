"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.

Hafeezah Binte Abdul Kasim
"""

import sqlite3



def customer_tickets(conn, customer_id):
    """
    Return a list of tuples:
    (film_title, screen, price)

    Include only tickets purchased by the given customer_id.
    Order results by film title alphabetically.
    """

    cursor = conn.cursor()
    query = '''SELECT films.title, screenings.screen, tickets.price FROM tickets 
    JOIN screenings on tickets.screening_id = screenings.screening_id 
    JOIN films ON screenings.film_id = films.film_id WHERE tickets.customer_id=? 
    ORDER BY films.title;'''
    cursor.execute(query,(customer_id,))
    return cursor.fetchall()


def screening_sales(conn):
    """
    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.

    """
    cursor = conn.cursor()
    query = '''SELECT screenings.screening_id, films.title, COUNT(tickets.ticket_id) FROM screenings 
    JOIN films ON screenings.film_id = films.film_id 
    LEFT JOIN tickets ON screenings.screening_id = tickets.screening_id 
    GROUP BY screenings.screening_id 
    ORDER BY COUNT(tickets.ticket_id) 
    DESC;'''
    cursor.execute(query)
    return cursor.fetchall()

def top_customers_by_spend(conn, limit):
    """
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.

    """
    cursor = conn.cursor()
    query = '''SELECT customers.customer_name, SUM(tickets.price) FROM customers 
    JOIN tickets ON customers.customer_id = tickets.customer_id 
    GROUP BY customers.customer_id 
    ORDER BY SUM(tickets.price) DESC LIMIT ?;'''
    cursor.execute(query,(limit,))
    return cursor.fetchall()