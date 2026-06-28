class Bank:

    def __init__(self):
        # List to store all customers
        self.customers = []

    # ---------------- SIGN UP ----------------
    def signup(self):
        user = {}

        user["Name"] = input("Enter your Name: ")
        user["Username"] = input("Enter Username: ").lower().strip()

        # Check if username already exists
        for customer in self.customers:
            if customer["Username"] == user["Username"]:
                print("Username already exists.")
                return

        user["Email"] = input("Enter Email: ")
        user["Password"] = input("Enter Password: ")

        try:
            balance = int(input("Enter Initial Balance: ₹"))

            if balance < 0:
                print("Balance cannot be negative.")
                return

            user["Balance"] = balance

        except ValueError:
            print("Please enter numbers only.")
            return

        self.customers.append(user)
        print("\nSignup Successful!")

    # ---------------- SIGN IN ----------------
    def signin(self):

        username = input("Enter Username: ").lower().strip()
        password = input("Enter Password: ")

        for user in self.customers:

            if user["Username"] == username and user["Password"] == password:

                print(f"\nWelcome {user['Name']}!")

                while True:

                    print("""
========== Banking Menu ==========
1. Deposit
2. Withdraw
3. Check Balance
4. Logout
==================================
""")

                    try:
                        choice = int(input("Enter your choice: "))
                    except ValueError:
                        print("Please enter numbers only.")
                        continue

                    if choice == 1:
                        self.deposit(user)

                    elif choice == 2:
                        self.withdraw(user)

                    elif choice == 3:
                        self.check_balance(user)

                    elif choice == 4:
                        print("Logged Out Successfully.")
                        break

                    else:
                        print("Invalid Choice.")

                return

        print("Invalid Username or Password.")

    # ---------------- DEPOSIT ----------------
    def deposit(self, user):

        try:
            amount = int(input("Enter Amount to Deposit: ₹"))

            if amount <= 0:
                print("Enter a valid amount.")
                return

            user["Balance"] += amount

            print("\nDeposit Successful!")
            print(f"Available Balance: ₹{user['Balance']}")

        except ValueError:
            print("Please enter numbers only.")

    # ---------------- WITHDRAW ----------------
    def withdraw(self, user):

        try:
            amount = int(input("Enter Amount to Withdraw: ₹"))

            if amount <= 0:
                print("Enter a valid amount.")
                return

            if amount > user["Balance"]:
                print("Insufficient Balance.")
                return

            user["Balance"] -= amount

            print("\nWithdrawal Successful!")
            print(f"Available Balance: ₹{user['Balance']}")

        except ValueError:
            print("Please enter numbers only.")

    # ---------------- CHECK BALANCE ----------------
    def check_balance(self, user):

        print("\n---------------------------")
        print(f"Available Balance : ₹{user['Balance']}")
        print("---------------------------")

    # ---------------- MAIN MENU ----------------
    def menu(self):

        while True:

            print("""
=================================
      BANK MANAGEMENT SYSTEM
=================================
1. Sign Up
2. Sign In
3. Exit
=================================
""")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter numbers only.")
                continue

            if choice == 1:
                self.signup()

            elif choice == 2:
                self.signin()

            elif choice == 3:
                print("\nThank You for using the Bank Management System.")
                print("Visit Again!")
                break

            else:
                print("Invalid Choice. Please try again.")


# ---------------- MAIN PROGRAM ----------------

bank = Bank()   # Object Creation
bank.menu()     # Calling menu method