
balance = 1000

def check_balance():
    print(f"Your current balance is: ${balance}")

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(f"You have deposited: ${amount}")
    else:
        print("Deposit amount must be positive.")

def withdraw(amount):
    global balance
    if amount > 0:
        if amount <= balance:
            balance -= amount
            print(f"You have withdrawn: ${amount}")
        else:
            print("Insufficient funds.")
    else:
        print("Withdrawal amount must be positive.")

def exit_program():
    print("Thank you for using the banking system. Goodbye!")
    exit()

def main():
    while True:
        print("\nPlease choose an option:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            withdraw(amount)
        elif choice == '4':
            exit_program()
        else:
            print("Invalid choice. Please try again.")

main()