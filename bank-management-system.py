import random


class Account:
    accounts = []
    toggleLoan = True

    def __init__(self, name, email, address, account_type):

        self.accountNo = random.randint(10000, 99999)
        self.name = name
        self.email = email
        self.address = address
        self.balance = 0
        self.type = account_type
        self.transactions = []
        self.loan_count = 0
        self.total_loan = 0

        Account.accounts.append(self)
        print(f"\nAccount created.")
        print(f"\nYour Account No: {self.accountNo}")

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposited ${amount} success.")

    def withdraw(self, amount):
        if 0 <= amount <= self.balance:
            self.balance -= amount
            print(f"\nWithdrew ${amount} success.")
        else:
            print("\nWithdrawal amount exceeded")

    def check_balance(self):
        print(f"\nCurrent Balance: ${self.balance}")

    def loan(self, amount):
        if self.toggleLoan == True and self.loan_count < 2:
            self.loan_count += 1
            self.balance += amount
            self.total_loan += amount
            print(f"\n Loaned ${amount} success.")
        else:
            print("\n Loan not available")

    def transactions_history(self):
        print("\nTransaction history:")
        for transaction in self.transactions:
            print(transaction)

    def transfer(self, receiver, amount):
        if receiver not in Account.accounts:
            print("\nAccount does not exist")
        else:
            if 0 <= amount <= self.balance:
                self.balance -= amount
                receiver.deposit(amount)
                print(
                    f"\n Successfully Transferred ${amount} to {receiver.name}")
                self.transactions.append(
                    f" transferred ${amount} to {receiver.name}")
            else:
                print("\n Invalid transfer amount")


class Bank:

    def delete_account(self, account_no):
        for account in Account.accounts:
            if account.accountNo == account_no:
                Account.accounts.remove(account)
                print(f"\nDeleted  Account No: {account_no}.")
                return
        print(f"\nAccount No: {account_no} not found.")

    def loanStatus(self, value):
        Account.toggleLoan = value

    def All_users(self):
        print("\nList of User Accounts:")
        for account in Account.accounts:
            print(f"Account No: {account.accountNo}, Name: {account.name}")

    def total_available_balance(self):
        TotalBalance = sum(account.balance for account in Account.accounts)
        print(f"\nTotal Available Balance: ${TotalBalance}")

    def total_loan(self):
        total_loan_taken = sum(
            account.total_loan for account in Account.accounts)
        print(f"\nTotal Loan Amount: ${total_loan_taken}")


current_user = None
adminPass = '1234'
admin_acc = False

while True:

    if current_user is None and not admin_acc:
        print("No user logged in!")
        ch = input("Register/login (R/L), Admin(A): ")
        if ch == "R":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            account_type = input("Enter account type: ")
            current_user = Account(name, email, address, account_type)

        elif ch == "L":
            account_number = int(input("Account number: "))
            for user in Account.accounts:
                if user.accountNo == account_number:
                    current_user = user
                    break
            if current_user is None:
                print("Account not found.")

        elif ch == "A":
            pass_input = input("Enter admin password: ")
            if pass_input == adminPass:
                admin_acc = True

        else:
            print("Invalid choice")

    else:

        if admin_acc:
            print("1. Create Account")
            print("2. Delete Account")
            print("3. All User")
            print("4. Total Balance")
            print("5. Total Loan")
            print("6. Loan Feature on/off")
            print("7. Exit")
            ch = input("Enter your choice: ")

            if ch == "1":
                name = input("Enter user's name: ")
                email = input("Enter user's email: ")
                address = input("Enter user's address: ")
                account_type = input("Enter user's account type: ")
                Account(name, email, address, account_type)

            elif ch == "2":
                account_no = int(input("Enter Account No to delete: "))
                Bank().delete_account(account_no)

            elif ch == "3":
                Bank().All_users()

            elif ch == "4":
                Bank().total_available_balance()

            elif ch == "5":
                Bank().total_loan()

            elif ch == "6":
                toggle_choice = input("Enter 'True'  or 'False' ")
                Bank.loanStatus(toggle_choice)

            elif ch == "7":
                admin_acc = False

        else:
            print(f"\nWelcome {current_user.name} !\n")
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Check Balance")
            print("4. Request to Loan")
            print("5. Transfer Money")
            print("6. Transaction History")
            print("7. Exit")
            ch = input("Enter your choice: ")

            if ch == "1":
                amount = float(input("Enter the amount to deposit: "))
                current_user.deposit(amount)

            elif ch == "2":
                amount = float(input("Enter the amount to withdraw: "))
                current_user.withdraw(amount)

            elif ch == "3":
                current_user.check_balance()

            elif ch == "4":
                amount = float(input("Enter the amount to loan: "))
                current_user.loan(amount)

            elif ch == "5":
                amount = float(input("Enter the amount to transfer: "))
                receiver_account_no = int(
                    input("Enter the receiver's Account No: "))
                for account in Account.accounts:
                    if account.accountNo == receiver_account_no:
                        current_user.transfer(account, amount)
                        break
                else:
                    print("Receiver not found.")

            elif ch == "6":
                current_user.transactions_history()

            elif ch == "7":
                current_user = None
