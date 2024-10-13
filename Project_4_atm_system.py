def show_balance():
    print(f"Your balance is $ {balance: .2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("That is not a valid amount!")
        return 0
    else:
        return amount
def withdraw():
    amount = float(input("Enter amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient funds")
    elif amount < 0:
        print("Amount must be greater than zero")
        return 0
    else:
        return amount
    

balance = 0
is_running = True

while is_running:
    print("Welcome to the Simple Bank App")
    print("1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    user = input("Enter your choice (1-4): ")
    if user == "1":
        show_balance()
    elif user == "2":
        balance += deposit()
    elif user == "3":
        balance -= withdraw()
    elif user == "4":
        is_running = False
    else:
        print("This is not a valid choice")

print("Nice banking with you! do have a great day.")
