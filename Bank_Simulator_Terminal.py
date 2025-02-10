# Dictionary to store user account details
user_account = {"pin": 0, "Account Name": "", "Account_number": 0, "Balance": 0}

# Dictionary to track user login status
user_status = {"status": False}

def create_accountNo():
    # Creates a new account with a 4-digit account number and PIN
    while True:
        try:
            user_input = int(input("Please enter a 4-digit account number: "))
            if 1000 <= user_input <= 9999:
                user_account["Account_number"] = user_input
                print(f"Account number {user_account['Account_number']} successfully created!")
                break
            else:
                print("Invalid account number. Enter a 4-digit number.")
        except ValueError:
            print("Account number can only contain numerical values (1-9).")
    
    while True:
        try:
            user_input = int(input("Enter a 4-digit PIN number: "))
            if 1000 <= user_input <= 9999:
                user_account["pin"] = user_input
                print("PIN successfully set!")
                main_function()
                break
            else:
                print("Invalid PIN. Must be exactly 4 digits.")
        except ValueError:
            print("PIN must be numeric.")

def login():
    # Authenticate the user by verifying account number and PIN
    # Prevents login if no account exists

    if user_account["Account_number"] == 0:
        print("No account found! Please sign up first.")
        main_function()
        return

    while True:
        try:
            user_input = int(input("Please enter your account number: "))
            if user_input == user_account["Account_number"]:
                print(f"Account number {user_account['Account_number']} confirmed.")
                break
            else:
                print("Invalid account number. Try again.")
        except ValueError:
            print("Enter numerical values only.")
        
    while True:
        try:
            user_input = int(input("Please enter your PIN: "))
            if user_input == user_account["pin"]:
                user_status["status"] = True
                print("Account PIN confirmed. Login successful.")
                Display_Account()
                break
            else:
                print("Invalid PIN. Try again.")
        except ValueError:
            print("Enter numerical values only.")

def Status():
    # Checks if the user is logged in; prompts login or sign-up if not
    if user_status["status"]:
        print(f"Account {user_account['Account_number']} is logged in.")
        main_function()
    else:
        print("No account found!\nWould you like to login or sign up?")
    
    while True:
        print("1. Login")
        print("2. Sign up")
        try:
            user_input = int(input("Choose an option: "))
            if user_input == 1:
                print("---Login---")
                login()
                break
            else:
                print("---Account Creation---")
                create_accountNo()
                break
        except ValueError:
            print("Enter numerical values only.")

def Display_Balance():
    # Displays the user's current balance
    print(f"Your balance is: ${user_account['Balance']}")
    input("Press Enter to return home.")
    Display_Account()

def Deposit_Money():
    # Allows the user to deposit money into their account
    while True:
        print("1. Deposit $10")
        print("2. Deposit $20")
        print("3. Deposit $50")
        print("4. Deposit $100")
        print("5. Deposit a custom amount")
        try:
            user_input = int(input("Select deposit option: "))
            if user_input == 1:
                user_account["Balance"] += 10
            elif user_input == 2:
                user_account["Balance"] += 20
            elif user_input == 3:
                user_account["Balance"] += 50
            elif user_input == 4:
                user_account["Balance"] += 100
            elif user_input == 5:
                deposit_amount = int(input("Enter deposit amount: $"))
                user_account["Balance"] += deposit_amount
            else:
                print("Invalid option. Try again.")
                continue
            print("Deposit successful!")
            Display_Account()
            break
        except ValueError:
            print("Enter numerical values only.")

def Withdraw_Money():
    # Allows the user to withdraw money from their account
    while True:
        if user_account["Balance"] <= 0:
            print("Insufficient funds.")
            Display_Account()
            break
        print("1. Withdraw $10")
        print("2. Withdraw $20")
        print("3. Withdraw $50")
        print("4. Withdraw $100")
        print("5. Withdraw a custom amount")
        try:
            user_input = int(input("Select withdrawal option: "))
            if user_input == 1 and user_account["Balance"] >= 10:
                user_account["Balance"] -= 10
            elif user_input == 2 and user_account["Balance"] >= 20:
                user_account["Balance"] -= 20
            elif user_input == 3 and user_account["Balance"] >= 50:
                user_account["Balance"] -= 50
            elif user_input == 4 and user_account["Balance"] >= 100:
                user_account["Balance"] -= 100
            elif user_input == 5:
                withdraw_amount = int(input("Enter withdrawal amount: $"))
                if withdraw_amount <= user_account["Balance"]:
                    user_account["Balance"] -= withdraw_amount
                else:
                    print("Insufficient balance.")
                    continue
            else:
                print("Invalid option or insufficient funds. Try again.")
                continue
            print("Withdrawal successful!")
            Display_Account()
            break
        except ValueError:
            print("Enter numerical values only.")

def Transfer_Money():
    # Placeholder function for future money transfer feature
    print("Feature not implemented yet.")

def main_function():
    # Displays the main menu and handles user selection
    while True:
        print("\n--- Main Menu ---")
        print("1. Create Account")
        print("2. Login")
        print("3. Check Status")
        print("4. Shutdown")
        try:
            user_input = int(input("Please choose an option: "))
            if user_input == 1:
                create_accountNo()
            elif user_input == 2:
                login()
            elif user_input == 3:
                Status()
            elif user_input == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Enter numerical values only!")

def Display_Account():
    # Displays the account menu and allows the user to choose an action
    while True:
        print("\n--- Account Menu ---")
        print("1. Display Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Logout")

        try:
            user_input = int(input("Please choose an option: "))
            if user_input == 1:
                Display_Balance()
            elif user_input == 2:
                Deposit_Money()
            elif user_input == 3:
                Withdraw_Money()
            elif user_input == 4:
                Transfer_Money()
            elif user_input == 5:
                print("Logging out...")
                user_status["status"] = False  # Reset login status
                break
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Enter numerical values only!")

# Start the banking system
main_function()
