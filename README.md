# 🚗 Safe Riding Car Alarm System

This project simulates a **combinational logic circuit** designed to enhance car safety by activating an alarm when seatbelt conditions are not met. The logic is based on a real-world scenario where the car should alert the driver if either front seat is occupied and the corresponding seatbelt is **not fastened** when the car is started.

---

## 📘 Problem Overview

The alarm system is governed by five input signals:

- `DRIV`: Active-HIGH (1) when the **driver** is seated.
- `PASS`: Active-HIGH (1) when the **passenger** is seated.
- `BELTD`: Active-LOW (0) when the **driver's seatbelt is unfastened**.
- `BELTP`: Active-LOW (0) when the **passenger's seatbelt is unfastened**.
- `IGN`: Active-HIGH (1) when the **ignition is ON**.

The alarm (`ALARM`) is **activated (LOW)** only under five specific conditions where the car is started and seatbelt safety is violated.

---

## ✅ Alarm Activation Logic

The alarm turns ON (`ALARM = 0`) only when **one of the following five conditions** is met:

1. Driver seated, passenger absent, both seatbelts unfastened.
2. Driver seated, passenger absent, driver unbelted, passenger belted.
3. Driver and passenger seated, both unbelted.
4. Driver and passenger seated, driver unbelted, passenger belted.
5. Driver and passenger seated, driver belted, passenger unbelted.

All other combinations result in `ALARM = 1` (OFF).

---

## 🧠 Design Approach

This project uses:

- **Problem-Solving Method (PSM)**: To break down the logic into manageable components.
- **Boolean Design Process (BDP)**: To derive the exact logic expression and simulate it using Python.

---

## 🧪 Simulation

The logic is implemented in Python using a simple function that checks the five exact alarm-triggering scenarios. A full test suite is included to verify all 16 possible input combinations against the expected output.

---

## 📂 Files Included

- `safeRidingCar1.py`: Contains the core logic function and test cases.
- `safeRidingCar2.py`: Contains the core logic function and test cases with enhanced version with the help of AI.
- `README.md`: Project overview and documentation.
- `logicCircuit.png`: contains the logic circuit diagram of the problem
- `flowchart.jpeg`: contains the flowchart

---


