import threading
import time
import random

class AnswerSheet:
    def __init__(self, id):
        self.id = id
        self.marks = None
        
class EvaluatorThread(threading.Thread):
    def __init__(self, sheet, lock):
        super().__init__()
        self.sheet = sheet
        self.lock = lock

    def run(self):
        time.sleep(random.uniform(0.5,1.5))
        marks = random.randint(30,100)
        with self.lock:
                self.sheet.marks = marks
                print(f"Sheet {self.sheet.id} evaluated: {marks}")

class ExamSystem:
    def start(self, num):
        sheets = [AnswerSheet(i) for i in range(1,num+1)]
        lock = threading.Lock()
        threads = [EvaluatorThread(s, lock) for s in sheets]
        
        for t in threads: t.start()
        for t in threads: t.join()
        avg = sum(s.marks for s in sheets)/len(sheets)
        print("Average:", avg)