import threading
import time
import random

class MonitoringDevice:
    def read_data(self):
        raise NotImplementedError 
    
class HeartRateMonitor(MonitoringDevice):
    def read_data(self):
        return f"Heart Rate: {random.randint(60, 100)} bpm"

class BloodPressureMonitor(MonitoringDevice):
    def read_data(self):
        return f"Blood Pressure: {random.randint(110, 140)}/{random.randint(70, 90)}"

class HospitalSystem:
    def __init__(self):
        self.running = True
        
    def start_monitoring(self):
        devices = [HeartRateMonitor(), BloodPressureMonitor()]
        threads = []
        
        for device in devices:
            t = threading.Thread(target=self.monitor, args=(device,))
            threads.append(t)
            t.start()
            
        time.sleep(5)
        self.running = False 
        
        for t in threads:
            t.join()

    def monitor(self, device):
        while self.running:
            print(device.read_data())
            time.sleep(1)