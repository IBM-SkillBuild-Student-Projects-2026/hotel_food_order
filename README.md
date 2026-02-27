# 🏨 Hotel Food Order System (Python)

This is a simple **command-line based Hotel Food Ordering System** written in **Python**.
It allows a customer to select food items from a predefined menu, calculates the total bill, applies GST, and displays the final amount to be paid.

---

## 📋 Features

* Displays a hotel menu with item numbers and prices
* Takes customer name and table number as input
* Allows multiple food items to be ordered
* Calculates:

  * Total amount
  * GST (5%)
  * Final payable amount
* Prints a simple bill at the end

---

## 🍽️ Menu Items

| Item No | Item Name | Price (₹) |
| ------: | --------- | --------- |
|       1 | Idli      | 40        |
|       2 | Dosa      | 60        |
|       3 | Vada      | 50        |
|       4 | Poori     | 70        |
|       5 | Tea       | 20        |
|       6 | Coffee    | 30        |

---

## 🛠️ Requirements

* Python 3.x
  (No external libraries required)

---

## ▶️ How to Run

1. Make sure Python is installed:

   ```bash
   python --version
   ```

2. Save the program as:

   ```bash
   hotel_food_order.py
   ```

3. Run the program:

   ```bash
   python hotel_food_order.py
   ```

---

## 🧾 How It Works

1. Enter customer name
2. Enter table number
3. View the hotel menu
4. Enter item numbers to order

   * Enter `0` to stop ordering
5. The program calculates:

   * Total bill
   * GST (5%)
   * Final amount
6. Bill is displayed on the screen

---

## 📌 Sample Output

```
------ HOTEL MENU ------
1 Idli - 40
2 Dosa - 60
3 Vada - 50
4 Poori - 70
5 Tea - 20
6 Coffee - 30

Enter item number to order (0 to stop): 2
Dosa added to your order

Enter item number to order (0 to stop): 5
Tea added to your order

------ BILL ------
Customer Name: Ravi
Ordered Items: ['Dosa', 'Tea']
Total Amount: 80
GST (5%): 4.0
Final Amount to Pay: 84.0
```

---

## 🚀 Possible Improvements

* Add quantity selection
* Store order history
* Add discount options
* Improve bill formatting
* Convert to GUI or web application
