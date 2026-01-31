# 2. Define class and constructor
class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        # 4. Encapsulation (private attributes)
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    # 3. Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f" Deposited {amount}. New Balance: {self.__balance}")
        else:
            print(" Invalid deposit amount.")

    # 3. Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f" Withdrawn {amount}. Remaining Balance: {self.__balance}")
        else:
            print("Insufficient balance.")

    # 3. Method to check balance
    def get_balance(self):
        return self.__balance

    # 3. Method to display account info
    def display(self):
        print(f"Account Holder: {self.__holder_name}")
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: {self.__balance}")


# .....................................................


# Inheritance + Method Overriding

# 5. Use inheritance
class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.05):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    # 6. Override method
    def deposit(self, amount):
        interest = amount * self.interest_rate
        total_amount = amount + interest
        super().deposit(total_amount)
        print(f"Interest Added: {interest}")



 # Creating Multiple Objects & Simulating Bank Operations

 # 7. Create multiple objects
account1 = BankAccount("BA101", "Ali", 1000)
account2 = SavingsAccount("SA201", "Sara", 2000)

print("\n--- Bank Account Operations ---")
account1.display()
account1.deposit(500)
account1.withdraw(300)

print("\n--- Savings Account Operations ---")
account2.display()
account2.deposit(1000)   # overridden method
account2.withdraw(500)

print("\nFinal Balances:")
print("Ali Balance:", account1.get_balance())
print("Sara Balance:", account2.get_balance())

