import threading
import time
import random
from queue import Queue

class Email:
    def __init__(self, address, subject):
        self.address = address
        self.subject = subject
        
class SenderThread(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue
        
    def run(self):
        while True:
            email = self.queue.get()
            if email == "STOP":
                break
            print(f"Sending to {email.address}: {email.subject}")
            time.sleep(random.uniform(0.5,1.2))
            print(f"Sent to {email.address}")
            self.queue.task_done()
class EmailServer:
    def start(self, emails):
        q = Queue()
        workers = [SenderThread(q) for _ in range(3)]
        for w in workers: w.start()
        
        for mail in emails:
            q.put(mail)
            
        q.join()
        for _ in workers: q.put("STOP")
        for w in workers: w.join()