#os - operating system
import os

# Define the file paths for the bank data and transaction log
bankDataFile = "Bank Data.txt"
transactionLogFile = "Transaction Log.txt"

# Check if the bank data file exists; if not, create it
if not os.path.exists(bankDataFile):
    with open(bankDataFile, "w") as f:
        f.write("0")

# Check if the transaction log file exists; if not, create it
if not os.path.exists(transactionLogFile):
    with open(transactionLogFile, "w") as f:
        f.write("")

# Load the current balance from the bank data file
with open(bankDataFile, "r") as f:
    balance = float(f.read())

# Define a function to handle deposits
def deposit(amount):
    if amount <= 10:
        print("Invalid deposit amount.")
        return
    global balance
    balance += amount
    with open(bankDataFile, "w") as f:
        f.write(str(balance))
    with open(transactionLogFile, "a") as f:
        f.write(f"Deposit: R{amount}\n")
    print(f"\nDeposit of R{amount} successful. \nCurrent balance: R{balance} \nThank you for banking with EverTrust.")

# Define a function to handle withdrawals
def withdraw(amount):
    if amount <= 10: #user cannot withdraw less than R10
        print("Invalid withdrawal amount.")
        return
    global balance
    if balance >= amount:
        balance -= amount
        with open(bankDataFile, "w") as f:
            f.write(str(balance))
        with open(transactionLogFile, "a") as f:
            f.write(f"Withdrawal: R{amount}\n")
        print(f"\nWithdrawal of R{amount} successful. \nCurrent balance: R{balance} \nThank you for banking with EverTrust.")
        
    else:
        print(f"Sorry, you do not have sufficient funds. Current balance: R{balance}")

# Define a function to display the current balance
def display_balance():
    with open(bankDataFile, "r") as f:
        balance = float(f.read())
    print(f"Current balance: R{balance}")

# Prompt the user for a transaction
print("==============================Welcome to EverTrust || A Bank That You Can TRUST==============================")
while True:
    #print("==============================Welcome to EverTrust || A Bank That You Can TRUST============================== \n ")
    print("\nWould you like to make a transaction?")
    answer = input("Yes or No: ")
    if answer.lower() == "yes":
        print("")
        display_balance()
        print("Would you like to make a deposit or withdrawal?")
        answer = input("Deposit or Withdrawal: ")
        if answer.lower() == "deposit":
            while True:
                try:
                    amount = float(input("How much would you like to deposit? "))
                    break
                except ValueError:
                    print("You provided an invalid input.")
            deposit(amount)
        elif answer.lower() == "withdrawal":
            while True:
                try:
                    amount = float(input("How much would you like to withdraw? "))
                    break
                except ValueError:
                    print("You provided an invalid input.")
            withdraw(amount)
        else:
            print("You provided an invalid input.")
    elif answer.lower() == "no":
            # Display the final balance
            print("")
            display_balance()
            print("Thank you for banking with EverTrust.")
            break
    else:
        print("You provided an invalid input.")






