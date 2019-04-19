import threading
class x(threading.Thread):
    def run(self):
        print("x thread"+" "+self.getName())
class y(threading.Thread):
    def run(self):
        print("y thread"+" "+self.getName())
x1=x()
x1.setName("x thread1")
x1.start()
x2=x()
x2.start()
y1=y()
y1.start()
