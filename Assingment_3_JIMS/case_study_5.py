import threading
import time

class ImageTask:
    def process(self):
        raise NotImplementedError
    
class ResizeTask(ImageTask):
    def process(self):
        print("Resizing image...")
        time.sleep(1)
        
class FilterTask(ImageTask):
    def process(self):
        print("Applying filter...")
        time.sleep(1)
        
class SaveTask(ImageTask):
    def process(self):
        print("Saving image...")
        time.sleep(1)
        
class Pipeline:
    def __init__(self):
        self.event1 = threading.Event()
        self.event2 = threading.Event()
        
def run(self):
    t1 = threading.Thread(target=self.resize)
    t2 = threading.Thread(target=self.filter)
    t3 = threading.Thread(target=self.save)
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
    
def resize(self):
    ResizeTask().process()
    self.event1.set() # trigger next step
    
def filter(self):
    self.event1.wait()
    FilterTask().process()
    self.event2.set()
    
def save(self):
    self.event2.wait()
    SaveTask().process()