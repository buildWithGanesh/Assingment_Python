import threading
import time

class Station:
    def work(self, item):
        raise NotImplementedError

class CuttingStation(Station):
    def work(self, item):
        print(f"Cutting item {item}")
        time.sleep(1)

class WeldingStation(Station):
    def work(self, item):
        print(f"Welding item {item}")
        time.sleep(1)

class PaintingStation(Station):
    def work(self, item):
        print(f"Painting item {item}")
        time.sleep(1)

class AssemblyLine:
    def __init__(self):
        self.event_cut = threading.Event()
        self.event_weld = threading.Event()

    def start_line(self, items):
        self.items = items
        
        t1 = threading.Thread(target=self.cutting_process)
        t2 = threading.Thread(target=self.welding_process)
        t3 = threading.Thread(target=self.painting_process)
        
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()

    def cutting_process(self):
        for item in self.items:
            CuttingStation().work(item)
        self.event_cut.set()

    def welding_process(self):
        self.event_cut.wait()
        for item in self.items:
            WeldingStation().work(item)
        self.event_weld.set()

    def painting_process(self):
        self.event_weld.wait()
        for item in self.items:
            PaintingStation().work(item)