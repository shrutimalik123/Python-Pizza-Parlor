# 🍕 Python Pizza Parlor - Order Management Sim

A fast-paced service simulator where you play as a pizza chef. Your goal is to accurately fulfill customer orders by selecting the correct toppings from your inventory. This project focuses on the logic required to compare two sets of data for equality, regardless of the order in which they were entered.

This project focuses on teaching:
* **List Normalization:** Using `sorted()` to ensure that "Peppers and Onions" matches "Onions and Peppers."
* **Sentinel Values:** Using a specific keyword (like "done") to exit an input loop.
* **Random Sampling:** Utilizing `random.sample()` to pull multiple unique items from a list without repetition.
* **Membership Testing:** Checking if a user's input exists within a pre-defined list of allowed options.

---

## ✨ Features

* **Dynamic Orders:** Customers order between 2 and 3 unique toppings every round.
* **Inventory Control:** The kitchen only accepts toppings that are actually on the menu.
* **Flexible Input:** Add as many toppings as you want; the game only checks your work when you say you're "done."
* **Scoring System:** Earn points for perfect matches and receive feedback on failed orders.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed on your system.

### 2. Setup and Execution
1.  **Save the Code:** Save the Python script as `pizza_parlor.py`.
2.  **Open Terminal:** Navigate to the folder where you saved the file.
3.  **Run the Script:**
    ```bash
    python pizza_parlor.py
    ```

### 3. Gameplay Instructions
1.  Read the customer's request carefully.
2.  Type a topping and press **Enter**.
3.  Repeat for all requested toppings.
4.  Type **"done"** to send the pizza to the customer.



---

## 🧠 Code Structure Highlights

### The Power of Sorting
Without `sorted()`, if a customer wanted `['mushrooms', 'peppers']` and you typed `['peppers', 'mushrooms']`, the game would say you failed. Sorting both lists into alphabetical order before comparing them fixes this!

```python
# Even if the order is different, sorted() makes them identical
if sorted(user_pizza) == sorted(customer_order):
    score += 100

