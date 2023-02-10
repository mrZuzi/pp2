import math 
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def change(self,newx,newy):
        self.x=newx
        self.y=newy
    def dist(self,point):
        dist=math.sqrt(pow((point.x-self.x),2)+pow((point.y-self.y),2))
        print(dist)
qqq=point(1,1)
bbb=point(2,2)
qqq.change(3,3)
qqq.dist(bbb)