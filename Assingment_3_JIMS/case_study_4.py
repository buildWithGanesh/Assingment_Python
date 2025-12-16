import threading
import time

class RailwayReservation:
    def __init__(self, seats):
        self.seats = seats
        self.lock = threading.Lock()
    def book_seat(self, user):
        with self.lock:
            if self.seats > 0:
                print(f"{user} booked a seat.")
                self.seats -= 1
            else:
                print(f"{user} failed to book. No seats left.")
                
class UserThread(threading.Thread):
    def __init__(self, name, system):
        super().__init__()
        self.user = name
        self.system = system
        
def run(self):
    self.system.book_seat(self.user)