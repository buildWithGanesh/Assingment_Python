import threading
import time
import random

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Deposited {amount} | Balance: {self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount} | Balance: {self.balance}")
            else:
                print("Insufficient Balance")

class TransactionThread(threading.Thread):
    def __init__(self, account):
        super().__init__()
        self.account = account

    def run(self):
        for _ in range(5):
            action = random.choice(["deposit", "withdraw"])
            amount = random.randint(10, 100)
        
        if action == "deposit":
            self.account.deposit(amount)
        else:
            self.account.withdraw(amount)
        time.sleep(0.5)