class Geeky:
    def __init__(self, id):
        self.id = id
 
manager = Geeky(100)
 
manager.__dict__['life'] = 498
 
x=manager.life + len(manager.__dict__)
 
print (x)
