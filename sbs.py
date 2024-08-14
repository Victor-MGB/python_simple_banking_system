# Simple Banking System Project

def create_account(accounts):
    username = input("Enter username for new account: ")
    if username in accounts:
        print("Account already exists!")
    else:
        accounts[username] = {"balance": 0, "transactions": []}
        print(f"Account for {username} created successfully!")

def deposit(accounts):
    username = input("Enter your username: ")
    if username in accounts:
        amount = float(input("Enter amount to deposit: "))
        accounts[username]["balance"] += amount
        accounts[username]["transactions"].append(f"Deposited: {amount}")
        print(f"Deposited {amount} into {username}'s account.")
    else:
        print("Account not found!")

def withdraw(accounts):
    username = input("Enter your username: ")
    if username in accounts:
        amount = float(input("Enter amount to withdraw: "))
        if accounts[username]["balance"] >= amount:
            accounts[username]["balance"] -= amount
            accounts[username]["transactions"].append(f"Withdrew: {amount}")
            print(f"Withdrew {amount} from {username}'s account.")
        else:
            print("Insufficient balance!")
    else:
        print("Account not found!")

def check_balance(accounts):
    username = input("Enter your username: ")
    if username in accounts:
        print(f"{username}'s balance: {accounts[username]['balance']}")
    else:
        print("Account not found!")

def main():
    accounts = {}
    
    while True:
        print("\nSimple Banking System")
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check balance")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            deposit(accounts)
        elif choice == '3':
            withdraw(accounts)
        elif choice == '4':
            check_balance(accounts)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
