class Shape:
    perimeter = 0
    type = "None"
    boundingBox = [0,0,0,0]  # x,y,l,h
    corners = 0
    area = 0

    def toString(self):
        out=""" Type: {} Area: {} Perimeter: {} Corners: {} """.format(self.type,self.area,self.perimeter,self.corners)
        return out

    
