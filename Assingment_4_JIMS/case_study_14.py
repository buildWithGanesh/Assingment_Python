import threading
import time
import random

class Taxi:
    def __init__(self, taxi_id):
        self.taxi_id = taxi_id
        self.available = True

class DispatchSystem:
    def __init__(self):
        self.taxis = [Taxi(i+1) for i in range(3)]
        self.lock = threading.Lock()
    def request_ride(self, user):
        with self.lock:
            for taxi in self.taxis:
                if taxi.available:
                    taxi.available = False
                    print(f"{user} assigned Taxi {taxi.taxi_id}")
                    threading.Thread(target=self.complete_ride, args=(taxi,user)).start()
                    return
            print(f"{user} waiting – no taxis available")
    def complete_ride(self, taxi, user):
        time.sleep(random.randint(1,3))
        with self.lock:
            taxi.available = True
            print(f"Taxi {taxi.taxi_id} completed ride for {user}")