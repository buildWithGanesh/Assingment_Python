import threading
import time
import random
from queue import Queue

class Chef(threading.Thread):
    def __init__(self, name, order_queue):
        super().__init__()
        self.name = name
        self.order_queue = order_queue
    def run(self):
        while True:
            order = self.order_queue.get()
            if order == "STOP":
                break
            print(f"{self.name} cooking {order}")
            time.sleep(random.uniform(0.5,1.5))
            print(f"{self.name} completed {order}")
            self.order_queue.task_done()

class Kitchen:
    def start(self, orders):
        order_queue = Queue()
        chefs = [Chef("Chef1",order_queue), Chef("Chef2",order_queue)]
        for c in chefs: c.start()
        
        for o in orders: order_queue.put(o)
        
        order_queue.join()
        for _ in chefs: order_queue.put("STOP")
        for c in chefs: c.join()