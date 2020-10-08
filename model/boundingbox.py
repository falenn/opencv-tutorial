class BoundingBox:
    x = 0
    y = 0
    w = 0
    h = 0

    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def width(self):
        return self.x+self.h

    def height(self):
        return self.y+self.h
