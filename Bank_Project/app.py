def deposit(user):
    try:
        amount = int(input("Enter the amount: ₹"))

        if amount > 0:
            user['Balance'] += amount
            print("Deposit Successful")
        else:
            print("Enter a valid amount")

    except ValueError:
        print("Please enter numbers only")


def withdraw(user):
    try:
        amount = int(input("Enter the amount: ₹"))

        if amount <= 0:
            print("Enter a valid amount")
            return

        if user['Balance'] >= amount:
            user['Balance'] -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    except ValueError:
        print("Please enter numbers only")


def check_balance(user):
    print(f"Your balance is ₹{user['Balance']}")


# List to store customers
customers = []

while True:
    print("""
========== Welcome to the Bank ==========
1. Sign Up
2. Sign In
3. Exit
""")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Sign Up
    if choice == 1:
        user = {}

        user['Name'] = input("Enter your name: ")
        user['Username'] = input("Enter username: ").lower().strip()

        # Check if username already exists
        exists = False
        for customer in customers:
            if customer['Username'] == user['Username']:
                exists = True
                break

        if exists:
            print("Username already exists.")
            continue

        user['Email'] = input("Enter email: ")
        user['Password'] = input("Enter password: ")

        try:
            user['Balance'] = int(input("Enter initial balance: ₹"))
        except ValueError:
            print("Invalid balance.")
            continue

        customers.append(user)
        print("Signup Successful!")

    # Sign In
    elif choice == 2:
        username = input("Enter username: ").lower().strip()
        password = input("Enter password: ")

        logged_in = False

        for user in customers:
            if username == user['Username'] and password == user['Password']:
                logged_in = True
                print(f"\nWelcome {user['Name']}!")

                while True:
                    print("""
------ Banking Menu ------
1. Deposit
2. Withdraw
3. Check Balance
4. Logout
""")

                    try:
                        option = int(input("Enter your option: "))
                    except ValueError:
                        print("Please enter a valid number.")
                        continue

                    if option == 1:
                        deposit(user)

                    elif option == 2:
                        withdraw(user)

                    elif option == 3:
                        check_balance(user)

                    elif option == 4:
                        print("Logged out successfully.")
                        break

                    else:
                        print("Invalid option.")

                break

        if not logged_in:
            print("Invalid Username or Password.")

    # Exit
    elif choice == 3:
        print("Thank you for using the Bank Application.")
        break

    else:
        print("Invalid choice.")
        
        
        
        
        
        
        