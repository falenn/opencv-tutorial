import model.boundingbox as BoundingBox

class Shape:
    perimeter = 0
    type = "None"
    boundingbox = None
    corners = 0
    area = 0

    def toString(self):
        out=""" Type: {} Area: {} Perimeter: {} Corners: {} """.format(self.type,self.area,self.perimeter,self.corners)
        return out

    def setBoundingBox(self,x,y,w,h):
        self.boundingbox = BoundingBox(x,y,w,h)

    def getBoundingBox(self):
        if self.boundingbox == None:
            return BoundingBox(0,0,0,0)


