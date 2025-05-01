import json
import os
from datetime import datetime

balance =1000.0
pin="1234"
transaction_history=[]

if os.path.exists("transaction.json"):
    with open("transaction.json","r") as file:
        transaction_history = json.load(file)
    print("Transaction history loaded successfully.")
else:
    print("No previous transaction history found. Starting fresh.")

max_attempts = 3
attempts=0
authenticated=False
while attempts< max_attempts:
    entered_pin = input("Enter your 4-digit PIN: ")
    if entered_pin == pin:
        authenticated=True
        print("Authentication successful.")
        break
    else:
        attempts += 1
        print(f"Incorrect PIN. You have {max_attempts - attempts} attempts left.")
if not authenticated:
    print("Too many incorrect attempts. Exiting.")
    
else:
    while True:
        print("\nWelcome to the ATM!")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit")
        print("6. Export Transaction History to File")

        choice = input("Please select an option (1-6): ")

        if choice == "1":
            print(f"Your current balance is: ${balance:.2f}")

        elif choice == "2":
            deposit_amount = float(input("Enter amount to deposit: $"))
            if deposit_amount > 0:
                balance += deposit_amount
                transaction_history.append({"date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "type": "Deposit", "amount": deposit_amount})
                print(f"Successfully deposited ${deposit_amount:.2f}. New balance: ${balance:.2f}")
            else:
                print("Invalid deposit amount.")

        elif choice == "3":
            withdraw_amount = float(input("Enter amount to withdraw: $"))
            if 0 < withdraw_amount <= balance:
                balance -= withdraw_amount
                transaction_history.append({"date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "type": "Withdrawal", "amount": withdraw_amount})
                print(f"Successfully withdrew ${withdraw_amount:.2f}. New balance: ${balance:.2f}")
            else:
                print("Invalid withdrawal amount or insufficient funds.")

        elif choice == "4":
            if transaction_history:
                print("\nTransaction History:")
                for transaction in transaction_history:
                    print(f"{transaction['date']} - {transaction['type']}: ${transaction['amount']:.2f}")
            else:
                print("No transactions found.")
        
        elif choice == "5":
            print("Exiting the ATM. Thank you!")
            break

        elif choice == "6":
            with open("transaction.json", "w") as file:
                json.dump(transaction_history, file)
            print("Transaction history saved. Exiting.")
            break

        else:
            print("Invalid option. Please try again.")


