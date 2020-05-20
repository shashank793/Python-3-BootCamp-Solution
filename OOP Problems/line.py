import math

class Line():
    def __init__(self,cord1,cord2):
        self.cord1 = cord1
        self.cord2 = cord2

    def disance(self):
        x1 = self.cord1[0]
        x2 = self.cord2[0]
        y1 = self.cord1[1]
        y2 = self.cord2[1]

        expr = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)
        return math.sqrt(expr)

    def slope(self):
        x1 = self.cord1[0]
        x2 = self.cord2[0]
        y1 = self.cord1[1]
        y2 = self.cord2[1]

        slope = (y2-y1)/(x2-x1)
        return slope

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.disance())
print(li.slope())