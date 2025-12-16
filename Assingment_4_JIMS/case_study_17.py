import threading
import time
import random

class Tank(threading.Thread):
    def __init__(self, tank_id):
        super().__init__()
        self.tank_id = tank_id
        self.level = random.randint(30,80)
        self.running = True
        
def run(self):
    while self.running:
        self.level += random.randint(-5,5)
        self.level = max(0, min(100, self.level))
        print(f"Tank {self.tank_id}: {self.level}%")

        if self.level < 20:
            print(f"ALERT: Tank {self.tank_id} LOW water!")
        elif self.level > 90:
            print(f"ALERT: Tank {self.tank_id} OVERFLOW!")
        time.sleep(1)

class TankMonitor:
    def start(self):
        tanks = [Tank(i+1) for i in range(3)]
        for t in tanks: t.start()
        
        time.sleep(7)
        
        for t in tanks:
            t.running = False
            t.join()