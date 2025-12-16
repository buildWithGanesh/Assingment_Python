import threading
import time
import random

class NewsSource:
    def __init__(self, name):
        self.name = name
    def download(self):
        time.sleep(random.uniform(0.5,1.5))
        return f"Headlines from {self.name}"
    
class NewsManager:
    def __init__(self, sources):
        self.sources = sources
        self.lock = threading.Lock()
        self.results = []

    def worker(self, source):
        news = source.download()
        with self.lock:
            self.results.append(news)
            print(news)

    def start(self):
        threads = []
        for s in self.sources:
            t = threading.Thread(target=self.worker, args=(s,))
            threads.append(t)
        for t in threads:
            t.start()
        for t in threads:
            t.join()