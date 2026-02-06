import sqlite3
# you will need to pip install pandas matplotlib
import pandas as pd
import matplotlib as mpl

def get_connection(db_path="orders.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def main():

    db = get_connection()
    while True:
        choice = menu()
        if choice == '1':
            product_category(db)
        elif choice == '2':
            total_customers(db)
        elif choice == '3':
            order_by_customer(db,email)
            email = input("Enter the email: ")
        elif choice == '4':
            under_two_pounds(db)
        elif choice == "Q":
            break

    db.close()

def menu():
    print("\n Choices")
    print("1: See all product categories in the database")
    print("2: View total number of customers")
    print("3: Show orders for a given customers - based on email")
    print("4: Display all products priced below £2")
    print("Q : Quit")

    choice = int(input('Enter your choice: '))
    return choice 

def product_category(db):
    query = "SELECT DISTINCT category FROM products;"
    df = pd.read_sql_query(query,db)
    print(df)

def total_customers(db):
    query = 'SELECT count(customer_id) FROM customers;'
    df = pd.read_sql_query(query,db)
    print(df)

def order_by_customer(db,email):
    query = ''

def under_two_pounds(db):


if __name__=="__main__":
    
    main()

