# ============================================================
# 🚀 CodeAlpha Internship Project - Task 2
# 🧮 Project Title: Next-Gen Stock Portfolio Tracker
# 👨‍💻 Created by: AhmadXCode
# ============================================================


import os
import time

print("📈 Welcome to the Next-Gen Stock Portfolio Tracker!\n")
print("─" * 55)

# Step 1: Get total number of stocks
while True:
    try:
        num_stocks = int(input("💡 How many different stocks do you own? ➤ "))
        if num_stocks <= 0:
            print("⚠️ Please enter a positive number.\n")
            continue
        break
    except ValueError:
        print("❌ Invalid input! Please enter a number.\n")

portfolio = {}

# Step 2: Get stock details
for i in range(1, num_stocks + 1):
    print(f"\n📊 Enter details for stock {i}:")
    name = input("   🏦 Stock name ➤ ").capitalize()
    while True:
        try:
            price = float(input("   💲 Current price per share ➤ "))
            quantity = int(input("   📦 Quantity owned ➤ "))
            break
        except ValueError:
            print("❌ Invalid input! Please enter valid numbers.\n")
    portfolio[name] = {'price': price, 'quantity': quantity}

# Step 3: Calculate total portfolio value
total_value = sum(stock['price'] * stock['quantity'] for stock in portfolio.values())

# Step 4: Display portfolio summary
print("\n" + "═" * 55)
print("📋 Your Portfolio Summary")
print("═" * 55)

for name, data in portfolio.items():
    value = data['price'] * data['quantity']
    print(f"💼 {name:<15} | Price: ${data['price']:<10.2f} | Qty: {data['quantity']:<5} | Value: ${value:.2f}")
    time.sleep(0.5)

print("─" * 55)
print(f"💰 Total Portfolio Value: ${total_value:.2f}")
print("─" * 55)

# Step 5: Final message
print("\n🚀 Thank you for using the Next-Gen Stock Portfolio Tracker!")
