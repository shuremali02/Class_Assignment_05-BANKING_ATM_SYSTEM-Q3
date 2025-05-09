# 🏧 OOP Assignment in Python: ATM Machine

## 📌 Task:

Create an ATM class in Python with basic banking features.

---

## 📦 Class: ATM

### 🧾 Attributes:

* balance – (Initial balance: *1000 rupees*)
* pin – (Set a default PIN, e.g., *1234*)

---

## 🛠 Methods:

### 1. check_pin(input_pin)

* Purpose: Verify if the entered PIN is correct.

### 2. check_balance()

* Purpose: Display the current account balance.

### 3. deposit(amount)

* Purpose: Add money to the balance *only if the PIN is correct*.

### 4. withdraw(amount)

* Purpose: Subtract money from balance *only if*:

  * The PIN is correct.
  * The balance is sufficient.

### 5. exit()

* Purpose: Exit or end the program.

---

## ⭐ Bonus Task (Extra Marks):

### 🧭 Menu-Based System:

Create a loop-based menu that allows the user to choose operations:


Welcome to ATM
Enter your PIN:
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit


* If the entered PIN is *incorrect, user should **not be allowed* to deposit or withdraw money.

---

## 📌 Instructions:

* The code should be *clean, **well-structured, and **commented*.
* Each method should be implemented *separately*.
* Ensure input validation:

  * No negative amounts for deposit or withdrawal.
  * Proper message for incorrect PIN.

---