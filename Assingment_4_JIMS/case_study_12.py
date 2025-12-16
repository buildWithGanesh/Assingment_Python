import threading
import time

class TrafficLight(threading.Thread):
    def __init__(self, name, shared_lock):
        super().__init__()
        self.name = name
        self.shared_lock = shared_lock
        self.running = True
        
    def run(self):
        while self.running:
            with self.shared_lock:
                print(f"{self.name}: GREEN")
            time.sleep(1)
            with self.shared_lock:
                print(f"{self.name}: YELLOW")
            time.sleep(0.5)
            with self.shared_lock:
                print(f"{self.name}: RED")
            time.sleep(1)
            
class TrafficSystem:
    def start(self):
        lock = threading.Lock()
        lights = [TrafficLight("North-South", lock),
                    TrafficLight("East-West", lock)]
        
        for l in lights: l.start()
        time.sleep(6)
        
        for l in lights:
            l.running = False
            l.join()