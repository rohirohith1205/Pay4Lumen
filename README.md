# Electricity-billing-System
DBMS project using python and Mysql 
The Electricity Bill Payment System is a GUI-based application developed using Python (Tkinter) and MySQL for managing electricity billing operations efficiently.
It enables administrators to manage customer details, register new connections, calculate bills automatically, and generate receipts

**👤Customer Management**
Add, update, delete, and search customer records
Store details like name, mobile, gender, address, etc.
Displays all customer entries in a searchable table

**⚙️ New Connection Module**
Register new electricity connections
Includes connection type (Residential / Commercial / Industrial)
Tracks load required, address, and application date
Linked directly to registered customers

**💡 Billing Module**

Automatically calculates bill amount based on:
Connection type:
Residential → ₹6/unit
Commercial → ₹8/unit
Industrial → ₹10/unit

Displays generated bills in a table
Allows payment marking and bill summaries

**📬 Inbox & Receipt Module**
Displays all past payment receipts
Fetches and displays customer, connection, and billing info
Generates and saves receipts automatically in the database

**🔐 Login & Authentication**
Secure login system for admin access
Passwords are masked for privacy

Tables:

**customers**
id (VARCHAR)
name (VARCHAR)
mobile (VARCHAR)
gender (VARCHAR)
address (TEXT)

**new_connection**
connection_id (INT)
customer_id (VARCHAR)
connection_type (VARCHAR)
load_required (INT)
address (TEXT)
application_date (DATE)

**bills**
bill_id (VARCHAR)
customer_id (VARCHAR)
conn_id (INT)
units (INT)
amount (FLOAT)
status (VARCHAR)

**receipt**
receipt_id (INT AUTO_INCREMENT)
bills_id (VARCHAR)
customers_id (VARCHAR)
connections_id (INT)
cust_name (VARCHAR)
conn_type (VARCHAR)
units (VARCHAR)
charge_pu (VARCHAR)
amount (VARCHAR)


**Login Page: Admin logs in securely.
Customer Module: Add or update customer records.
New Connection: Assign a connection ID and type.
Billing Module: Fetch units and generate bills automatically.
Inbox: View or print receipts for completed payments.**
