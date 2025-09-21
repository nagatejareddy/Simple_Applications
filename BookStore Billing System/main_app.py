import sqlite3

# Connect to the database
conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()

# Take input from user
title = input("Enter the book title: ")
quantity = int(input("Enter the number of copies: "))

# Fetch price
cursor.execute("SELECT price FROM books WHERE title = ?", (title,))
result = cursor.fetchone()

if result:
    price = result[0]
    total = price * quantity
    print(f"\nBook: {title}")
    print(f"Price per copy: Rs. {price}")
    print(f"Quantity: {quantity}")
    print(f"Total Amount: Rs. {total}")
else:
    print("Sorry, the book is not available in the database.")

# Close connection
conn.close()
