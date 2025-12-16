from asyncio import threads
import threading
import time

class DeliveryAgent:
    def __init__(self, agent_id, order_id):
        self.agent_id = agent_id
        self.order_id = order_id
    def deliver(self):
        print(f"Agent {self.agent_id} started delivering Order {self.order_id}")
        time.sleep(2)
        print(f"Agent {self.agent_id} completed Order {self.order_id}")

class OrderManager:
    def __init__(self, orders):
        self.orders = orders
    def start_delivery(self):
        threads = []
        for i, order in enumerate(self.orders):agent = DeliveryAgent(i + 1, order)
        t = threading.Thread(target=agent.deliver)
        threads.append(t)
        t.start()
    for t in threads:t.join()
        
    print("All orders delivered!")