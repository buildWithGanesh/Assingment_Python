import threading
import time
import random

class ATM:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def withdraw(self, user, amount):
        with self.lock:
            if self.balance >= amount:
                print(f"{user} withdrawing {amount}")
                time.sleep(0.5)
                self.balance -= amount
                print(f"{user} completed. Balance = {self.balance}")
            else:
                print(f"{user} failed. Insufficient funds.")

class CustomerThread(threading.Thread):
    def __init__(self, atm, user):
        super().__init__()
        self.atm = atm
        self.user = user

    def run(self):
        for _ in range(3):
            amt = random.randint(50, 200)
            self.atm.withdraw(self.user, amt)