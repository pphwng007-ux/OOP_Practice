import math

class Point:
    def __init__(self, x = 0, y = 1):
        self.__x = x
        self.__y = y
        
    def read(self):
        x, y, color = input().split()
        super().__init__(int(x), int(y))
        self.color = color
        
    def print(self):
        print(f"({self.__x}, {self.__y})")
        
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy
        
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def distance(self):
        return math.sqrt(self.__x**2 + self.__y**2)
    
    def distance_to_point(self, P):
        return math.sqrt((self.__x - P.getX())**2 + (self.__y - P.getY())**2)
    
class ColorPoint(Point):

    def __init__(self, *args):

        # ColorPoint()
        if len(args) == 0:
            super().__init__(0, 1)
            self.color = "xanh"

        # ColorPoint(ColorPoint cp)
        elif len(args) == 1 and isinstance(args[0], ColorPoint):

            cp = args[0]

            super().__init__(cp.getX(), cp.getY())
            self.color = cp.color

        # ColorPoint(x, y, color)
        elif len(args) == 3:

            x, y, color = args

            super().__init__(x, y)
            self.color = color

    def read(self):

        data = input().split()
        
        self._Point__x = int(data[0])
        self._Point__y = int(data[1])
        self.color = data[2]
        
        
    def print(self):
        print(f"({self.getX()}, {self.getY()}): {self.color}")
        
    def __str__(self):
        return f"({self.getX()}, {self.getY()}): {self.color}"
    
    def setcolor(self, color):
        self.color = color
        
class ColorPointTest:
    def testCase(self):
        c1 = ColorPoint(); c1.print()
        c2 = ColorPoint(); c2.read(); c2.print()
        c3 = ColorPoint(c2)
        c2.move(5, 5); c2.print(); c3.print()
        