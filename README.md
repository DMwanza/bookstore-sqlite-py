# Book Store Management 

## Introduction
The **JESMA 9 Book Store Management** CLI application is designed to provide a user-friendly interface for managing a book store's inventory, processing sales, and maintaining customer records. The application is implemented in Python and uses the SQLAlchemy library to interact with a SQLite database, allowing for efficient storage and retrieval of data.

## Installation
To run the **JESMA 9 Book Store Management** application, please follow these steps:

1. Make sure Python is installed on your system. You can download and install Python from the [official Python website](https://www.python.org).
2. Install the necessary dependencies by running the following command in your terminal or command prompt:

## Getting Started
To start using the **JESMA 9 Book Store Management** application, follow these steps:

1. Save the provided code in a Python file with a `.py` extension, for example, `models.py`.
2. Open your terminal or command prompt and navigate to the directory where you saved the `models.py` file.
3. Run the script by typing the following command and press Enter:


The application will start running, and you will see the main menu options in the terminal. From there, you can input your choices and follow the prompts to perform various tasks in the bookstore management application.

## Database Structure
The application uses a SQLite database to store book information, customer details, and sales data. The database consists of three tables: **books**, **customers**, and **sales**. Below is an overview of the table structure:

### Books
- **id**: Unique identifier for the book.
- **title**: The title of the book.
- **author**: The author of the book.
- **genre**: The genre/category of the book.
- **publication_date**: The publication date of the book.
- **price**: The price of the book.
- **quantity**: The quantity of the book in stock.

### Customers
- **id**: Unique identifier for the customer.
- **name**: The name of the customer.
- **contact**: The contact information of the customer.

### Sales
- **id**: Unique identifier for the sale.
- **book_id**: Foreign key referencing the **books** table.
- **customer_id**: Foreign key referencing the **customers** table.
- **quantity**: The quantity of books sold.
- **sale_date**: The date and time of the sale.

## Functionality
The **Book Store Management** application provides the following functionality:

### 1. Add Book
Allows the user to add a new book to the inventory. The user is prompted to enter the book's title, author, genre, publication date, price, and quantity. The book is then added to the database.

### 2. Update Book Quantity
This option allows you to update the quantity of a book in the inventory.
Enter the ID of the book to update.
Enter the new quantity for the book.
The book quantity will be updated in the database.
### 3. List Books
Displays a list of all books in the inventory. The book information includes the ID, title, author, genre, publication date, price, and quantity.

### 4. Delete Book
This option allows you to delete a book from the inventory.
Enter the ID of the book to delete.
The book will be removed from the database.
### 5. Search Books
Enables the user to search for books based on a keyword. The application retrieves and displays books whose titles, authors, or genres match the keyword entered by the user.

### 6. Process Sale
Allows the user to process a sale by specifying the book ID, customer ID, and quantity. The application verifies the availability of the requested quantity in stock, updates the inventory, and records the sale in the database.

### 7. Add Customer
Enables the user to add a new customer to the database. The user is prompted to enter the customer's name and contact information, and the details are stored in the **customers** table.

### 8. List Customers
Displays a list of all customers in the database. The customer information includes the ID, name, and contact details.

### 9. Generate Report
This option generates a sales report.
The total number of sales and the total revenue are displayed.
### 10.Quit
This option exits the Book Store Management System.
Thank you for using the Book Store Management System!
