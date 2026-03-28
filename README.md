# Inventory Management System (Python CLI)

CLI inventory management system developed in Python as part of a RIWI learning project. The system evolves weekly, adding new features and improving structure.

---

## 📌 Project Overview

This project is a console-based inventory system that allows users to manage products, calculate statistics, and persist data using CSV files.

---

## 🚀 Features

### Week 1

* Register product (name, price, quantity)
* Calculate total cost
* Input validation
* Console output formatting

### Week 2

* Interactive menu system
* Add multiple products
* Show inventory
* Calculate basic statistics
* Use of lists and dictionaries

### Week 3

* Full CRUD system:

  * Add product
  * Show inventory
  * Search product
  * Update product
  * Delete product
* Advanced statistics:

  * Total units
  * Total value
  * Most expensive product
  * Highest stock product
* CSV persistence:

  * Save inventory to file
  * Load inventory from file
  * Merge or overwrite data
* Error handling and input validation
* Modular architecture

---

## 🧱 Project Structure

```
app.py                # Main application (menu and user interaction)
servicios_week3.py   # Inventory logic (CRUD + statistics)
archivos.py          # CSV file handling
docs/                # Flowcharts and documentation
README.md            # Project documentation
```

---

## 🧠 Technologies Used

* Python
* CSV file handling
* Lists and dictionaries
* Functions and modular programming

---

## ▶️ How to Run

1. Open terminal
2. Navigate to project folder
3. Run:

```
python app.py
```

---

## 💾 CSV Format

```
nombre,precio,cantidad
Laptop,1000,2
Mouse,50,3
```

---

## ⚠️ Notes

* The program validates user input to prevent crashes.
* Invalid CSV rows are ignored and counted.
* Inventory can be merged or overwritten when loading data.

---

## 📚 Learning Goals

* Understand control flow (if, while, for)
* Work with data structures (lists and dictionaries)
* Apply modular programming
* Handle files using CSV
* Implement error handling

---

## 👨‍💻 Author

The coder is Daniel David Martinez Gonzalez - Python learning project