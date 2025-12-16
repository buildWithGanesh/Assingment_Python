import threading
import time
import random

class Stock:
    def __init__(self, name):
        self.name = name
        self.running = True
        
    def update_price(self):
        while self.running:
            price = random.uniform(100, 500)
            print(f"{self.name} Price: {round(price,2)}")
            time.sleep(1)
            
class StockManager:
    def __init__(self):
        self.stocks = [Stock("AAPL"), Stock("TSLA"), Stock("GOOGL")]
        self.threads = []
    def start(self):
        for s in self.stocks:
            t = threading.Thread(target=s.update_price)
            self.threads.append
            t.start()
            
        time.sleep(5)
        
        for s in self.stocks:
            s.running = False
        
        for t in self.threads:
            t.join()