import sqlite3

# Connect (or create) the database
conn = sqlite3.connect("bookstore.db")
cursor = conn.cursor()

# Create the books table
cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    price REAL NOT NULL
                )''')

# Insert sample data
books_data = [
    ("Think Python", "Allen B. Downey", 475.0),
    ("Python Crash Course", "Eric Matthes", 650.0),
    ("Learning Python", "Mark Lutz", 800.0),
    ("Automate the Boring Stuff with Python", "Al Sweigart", 500.0)
]

cursor.executemany("INSERT INTO books (title, author, price) VALUES (?, ?, ?)", books_data)

# Commit and close
conn.commit()
print("Database created and data inserted successfully!")
conn.close()
