class shape():
    def area1():
        print (0)
class square(shape):
    def __init__(self,length):
        self.length = length
    def area1(self):
        print(self.length*self.length)
class rectangle(shape):
    def __init__(self,length ,width):
        self.length =length 
        self.width=width
    def area1(self):
        print(self.length*self.width)
area=rectangle(length=12, width=13)
area.area1()