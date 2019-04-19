import threading
import time
class x(threading.Thread):
    def run(self):
        for p in range(1,10):
            print(p)
class y(threading.Thread):
    def run(self):
        time.sleep(10)
        for q in range(11,20):
            print(q)
x1=x()
x1.start()
y1=y()
y1.start()
            
        
        
