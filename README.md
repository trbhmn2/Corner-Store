# Corner-Store
A full-featured inventory and sales management system built in high school for a student-run corner store. Includes a Streamlit dashboard for analytics, PHP frontend for purchase confirmation, and MySQL database integration.


# 🛒 Corner Store Management System (High School Project)

This repository contains a complete inventory and sales analytics system built for a student-run corner store. The project integrates multiple technologies including **Python**, **Streamlit**, **MySQL**, and **PHP**, and was developed during high school to support real-world retail operations.

---

## 📦 Features

### 🧠 Inventory & Sales Dashboard (Streamlit)
- Built in Python using Streamlit
- Connects to a live MySQL database
- Displays analytics on:
  - Total revenue and profit
  - Item-level statistics (bought quantity, revenue, profit)
  - Time-based profit trends
  - Custom graphs (selectable axes)
- Includes a sidebar form to add new items to the inventory

### 🛍️ Purchase Flow (PHP)
- `confirm_purchase.php` handles customer purchase confirmation
- `database_inc.php` securely connects to the MySQL database

### 🗃️ MySQL Database
- Tables used:
  - `items`: Product name, price, type, and ID
  - `recipt`: Transaction log, date, item sold, quantity, and revenue
- Clean integration using `pymysql` for Python and `mysqli` for PHP

---

## 📁 File Overview

| File/Folder           | Description                                    |
|----------------------|------------------------------------------------|
| `something.py`       | Main Streamlit app for analytics and inventory |
| `confirm_purchase.php` | PHP purchase confirmation handler              |
| `database_inc.php`   | Secure DB connection for PHP                    |
| `requirements.txt`   | Python dependencies (if included)              |

---

## 🧪 How to Run

### 🔧 Python (Streamlit)

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate


🌐 PHP
Place PHP files on a local server (e.g. XAMPP, MAMP).
Configure database_inc.php with your MySQL credentials.
Navigate to confirm_purchase.php in your browser to simulate checkout.
📚 What I Learned

Working with real-time data and databases
Backend/frontend integration across Python and PHP
Visualizing business metrics using Streamlit
Structuring scalable, modular codebases
Real-world project and teamwork responsibilities
