class Box:
    def __init__(self, w, l, h):
        self.w = w
        self.l = l
        self.h = h

    def __str__(self):
        msg = '(' + str(self.w) + ',' + str(self.l) + ',' + str(self.h) + ')'
        return msg

    def getWidth(self):
        return self.w
    
    def getLength(self):
        return self.l

    def getHeight(self):
        return self.h
    
    def setWidth(self):
        self.w = w

    def setLength(self):
        self.l = l

    def setHeight(self):
        self.h = h


b1 = Box(100,100,100)
print(b1)
print('상자의 부피는 ', b1.getWidth() * b1.getLength() * b1.getHeight())



    

    
        



    
        
