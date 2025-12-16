import threading
import time
import random

class Baggage:
    def __init__(self, bag_id, weight):
        self.bag_id = bag_id
        self.weight = weight
        
class ConveyorBelt(threading.Thread):
    def __init__(self, belt_id):
        super().__init__()
        self.belt_id = belt_id
        self.queue = []
        self.lock = threading.Lock()
        self.running = True

    def add_baggage(self, bag):
        with self.lock:
            self.queue.append(bag)

    def run(self):
        while self.running:
            with self.lock:
                if self.queue:
                    bag = self.queue.pop(0)
                else:
                    bag = None
                    
            if bag:
                print(f"Belt {self.belt_id} processing Bag {bag.bag_id}")
                time.sleep(bag.weight * 0.1)
                print(f"Belt {self.belt_id} finished Bag {bag.bag_id}")
            else:
                time.sleep(0.2)

class AirportSystem:
    def __init__(self, num_belts):
        self.belts = [ConveyorBelt(i+1) for i in range(num_belts)]
        for belt in self.belts:
            belt.start()

    def assign_baggage(self, bags):
        i = 0
        for bag in bags:
            self.belts[i].add_baggage(bag)
            i = (i + 1) % len(self.belts)

    def stop(self):
        for belt in self.belts:
            belt.running = False
        for belt in self.belts:
            belt.join()