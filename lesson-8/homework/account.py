import os

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_string(self):
        return f"{self.account_number},{self.name},{self.balance}"

    def from_string(data):
        account_number, name, balance = data.split(',')
        return Account(int(account_number), name, float(balance))

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = len(self.accounts) + 1
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        return account_number

    def view_account(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            return vars(account)
        else:
            return None

    def deposit(self, account_number, amount):
        if account_number in self.accounts and amount > 0:
            self.accounts[account_number].balance += amount
            self.save_to_file()
            return True
        return False

    def withdraw(self, account_number, amount):
        if account_number in self.accounts and 0 < amount <= self.accounts[account_number].balance:
            self.accounts[account_number].balance -= amount
            self.save_to_file()
            return True
        return False

    def save_to_file(self):
        with open('accounts.txt', 'w') as file:
            for account in self.accounts.values():
                file.write(account.to_string() + '\n')

    def load_from_file(self):
        if os.path.exists('accounts.txt'):
            with open('accounts.txt', 'r') as file:
                for line in file:
                    account = Account.from_string(line.strip())
                    self.accounts[account.account_number] = account

if __name__ == "__main__":
    bank = Bank()
    while True:
        print("1. Create Account\n2. View Account\n3. Deposit\n4. Withdraw\n5. Exit")
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                name = input("Enter name: ")
                while not name:
                    name = input("Enter name: ")
                while True:
                    initial_deposit = input("Enter initial deposit: ")
                    try:
                        initial_deposit = float(initial_deposit)
                        account_number = bank.create_account(name, initial_deposit)
                        print(f"Account created successfully. Your account number is {account_number}.")
                        break
                    except ValueError:
                        print('Enter valid deposit')
                        continue

            elif choice == 2:
                while True:
                    account_number = input("Enter account number: ")
                    try:
                        account_number = float(account_number)
                        account = bank.view_account(account_number)
                        if account:
                            print(f"Account Number: {account['account_number']}, Name: {account['name']}, Balance: {account['balance']}")
                        else:
                            print("Account not found.")
                        break
                    except ValueError:
                        print('Enter valid account number')
                        continue
                
            elif choice == 3:
                while True:
                    account_number = input("Enter account number: ")
                    try:
                        account_number = int(account_number)
                        break
                    except ValueError:
                        print('Enter valid account number')
                        continue
                while True:
                    amount = input("Enter amount to deposit: ")
                    try:
                        amount = float(amount)
                        break
                    except ValueError:
                        print('Enter valid amount')
                        continue
                
                if bank.deposit(account_number, amount):
                    print("Deposit successful.")
                else:
                    print("Deposit failed.")

            elif choice == 4:
                while True:
                    account_number = input("Enter account number: ")
                    try:
                        account_number = int(account_number)
                        break
                    except ValueError:
                        print('Enter valid account number')
                        continue
                while True:
                    amount = input("Enter amount to deposit: ")
                    try:
                        amount = float(amount)
                        break
                    except ValueError:
                        print('Enter valid amount')
                        continue
                if bank.withdraw(account_number, amount):
                    print("Withdrawal successful.")
                else:
                    print("Withdrawal failed.")

            elif choice == 5:
                break

            else:
                print("Invalid choice.")
        except ValueError:
            print('Enter only numbers between 1 to 5')