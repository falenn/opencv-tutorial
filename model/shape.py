from model.boundingbox import BoundingBox

class Shape:
    perimeter = 0
    type = "None"
    boundingbox = BoundingBox(0,0,0,0)
    corners = 0
    area = 0

    #def __init__(self):
    

    def toString(self):
        out=""" Type: {} Area: {} Perimeter: {} Corners: {} """.format(self.type,self.area,self.perimeter,self.corners)
        return out

    def setBoundingBox(self,x,y,w,h):
        self.boundingbox = BoundingBox(x,y,w,h)

    def getBoundingBox(self):
        return self.boundingbox 


