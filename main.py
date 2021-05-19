
class Shapes:
    def __init__(self, name, side):
        self.name = name
        self.side = side

    def area(self):
        return "I am a : " + self.name + "\n" + "I have " + self.side + "sides"


obj_shape = Shapes("shape", "so many ")
print(obj_shape.area())


class Rectangle(Shapes):
    def __init__(self, len1, wid1):
        self.length = len1
        self.width = wid1

    def area(self):
        result = self.length * self.width
        return result


obj_book = Rectangle(10, 5)
obj_screen = Rectangle(30, 9)
print("The area of a book is " + str(obj_book.area()))
print("The area of a screen is " + str(obj_screen.area()))


class Circle(Shapes):
    def __init__(self, pi1, rad1):
        self.pi = pi1
        self.radius = rad1

    def area(self):
        answer = self.pi * (self.radius)**2
        return answer


obj_bucket = Circle(3.14, 9)
print("The area of a bucket is " + str(obj_bucket.area()))


class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        output = 1/2 * self.base * self.height
        return output


obj_tri = Triangle(14, 10)
print("The area of a triangle is " + str(obj_tri.area()))
