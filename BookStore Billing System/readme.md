# 📚 BookStore Billing System (Python + SQLite)

## 📖 Introduction

This project is a simple **Bookstore Billing System** built using **Python** and **SQLite**.
It allows you to:

* Maintain a database of books (title, author, and price).
* Add book details into the database programmatically.
* Accept input from the user for a book title and quantity.
* Fetch book price from the database and calculate the total bill.

This project demonstrates how to **connect Python with SQLite**, create tables, insert data, and run SQL queries.

---

## 📂 Project Structure

```
BookStore-Billing-System/
│
├── create_db.py      # Script to create the database and insert sample books
├── main_app.py       # Script to accept user input and calculate total bill
├── bookstore.db      # SQLite database file (auto-created after running create_db.py)
└── README.md         # Project documentation
```

---

## ⚙️ Setup Instructions

1. Make sure you have **Python 3.x** installed.
2. Clone this repository or download the project folder.
3. Run the following command to create the database and insert sample books:

   ```bash
   python create_db.py
   ```
4. Now run the main application:

   ```bash
   python main_app.py
   ```

---

## 🛠️ How It Works

1. **Database Creation**

   * `create_db.py` creates a `bookstore.db` file.
   * It defines a table `books` with the fields:

     * `book_id` (Primary Key)
     * `title`
     * `author`
     * `price`

2. **Adding Data**

   * A list of sample books is inserted into the database automatically.

3. **Billing System**

   * `main_app.py` asks the user to enter:

     * Book title
     * Quantity of copies
   * It fetches the price of the book from the database using a `SELECT` query.
   * Calculates the **total amount** and displays the bill.

---

## 🖥️ Sample Output

**Input:**

```
Enter the book title: Think Python
Enter the number of copies: 2
```

**Output:**

```
Book: Think Python
Price per copy: Rs. 475.0
Quantity: 2
Total Amount: Rs. 950.0
```

---

## 🎯 Learning Outcomes

* Creating a **SQLite database** with Python.
* Using **INSERT** and **SELECT** SQL queries through Python.
* Building a simple billing system with real-time calculations.

---
