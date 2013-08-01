# Shape Area and Perimeter Classes
# Create an abstract class called Shape and then inherit
# from it other shapes like diamond, rectangle, circle, triangle etc.
# Then have each class override the area and perimeter functionality to handle each shape type.

import math


class Shape(object):
    def __init__(self):
        self.area = 0.0
        self.perimeter = 0.0

    def calc_area(self):
        pass

    def calc_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, w, l):
        super(Rectangle, self).__init__()
        self.w = w
        self.l = l

    def calc_area(self):
        self.area = self.w * self.l
        return self.area

    def calc_perimeter(self):
        self.perimeter = 2 * self.w + 2 * self.l
        return self.perimeter


class Circle(Shape):
    def __init__(self, r):
        super(Circle, self).__init__()
        self.r = r

    def calc_area(self):
        self.area = math.pi * (self.r ** 2)
        return self.area

    def calc_perimeter(self):
        self.perimeter = 2 * math.pi * self.r
        return self.perimeter


class Triangle(Shape):
    def __init__(self, b, s2, s3, h):
        self.b = b
        self.s2 = s2
        self.s3 = s3
        self.h = h

    def calc_area(self):
        self.area = 0.5 * self.b * self.h
        return self.area

    def calc_perimeter(self):
        self.perimeter = self.b + self.s2 + self.s3
        return self.perimeter


s = Rectangle(10, 20)
print "Rectangle - area: %.2f\tperimeter: %.2f" % (s.calc_area(), s.calc_perimeter())

c = Circle(2)
print "Circle - area: %.2f\tperimeter: %.2f" % (c.calc_area(), c.calc_perimeter())

t = Triangle(3, 2, 2, 2.5)
print "Triangle - area: %.2f\tperimeter: %.2f" % (t.calc_area(), t.calc_perimeter())


