import threading
import time
class x(threading.Thread):
    def run(self):
        time.sleep(10)
        self.s=0
        for p in range(1,10):
            self.s=self.s+p
class y(threading.Thread):
    def __init__(self,x1):
        self.x1=x1
        super().__init__()
    def run(self):
        for q in range(11,20):
            print(q)
            if q==15:
                self.x1.join()
                print(self.x1.s)
x1=x()
x1.start()
y1=y(x1)
y1.start()
