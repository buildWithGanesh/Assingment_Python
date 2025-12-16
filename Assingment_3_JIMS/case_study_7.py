import threading
import time

class Appliance:
    def run(self):
        raise NotImplementedError
    
class Light(Appliance):
    def run(self):
        while True:
            print("Light is ON")
            time.sleep(1)

class AC(Appliance):
    def run(self):
        while True:
            print("AC Cooling…")
            time.sleep(1.5)

class Washer(Appliance):
    def run(self):
        while True:
            print("Washer Running…")
            time.sleep(2)

class SmartHomeHub:
    def __init__(self):
        self.appliances = [Light(), AC(), Washer()]
        self.threads = []

    def start(self):
            for a in self.appliances:
                t = threading.Thread(target=a.run, daemon=True)
                self.threads.append(t)
                t.start()
            time.sleep(6)
            print("Smart Home Monitoring Ended")