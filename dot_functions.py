from math import sqrt


class Dot:
    def __init__(self, x, y, image):
        self.setCoordinates(x, y)
        self.setDotName("")
        self.parent = False
        self.childs = []
        self.red = 0
        self.image = image
        self.setRedValue()
        self.distance_between_start = 0

    def distance_pointsTo(self, end_point):

        width, height = self.image.size
        distance_points = 0
        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if self.x + i > 0 and self.x + i < width and self.y + j > 0 and self.y + j < height:
                    red = self.find_redOfPixel(self.x + i, self.y + j)
                    if red == 0:
                        distance_points = distance_points + 1
                    else:
                        distance_points = distance_points + 1.0 / (red)
                else:
                    distance_points = distance_points + 1
        diagonal = width * width + height * height
        dist = (end_point.x - self.x) ** 2 + (end_point.y - self.y) ** 2
        diagonal = sqrt(diagonal)
        dist = sqrt(dist)

        return (distance_points) ** 5 * (dist / diagonal)

    def setRedValue(self):
        self.red = self.find_redOfPixel(self.x, self.y)

    def find_red(self):
        return self.red

    def find_redOfPixel(self, x, y):
        r, g, b = self.image.getpixel((x, y))
        return r

    def add_parent(self, parent1):
        self.parent = parent1

    def getParent(self):
        return self.parent

    def add_child(self):
        width, height = self.image.size

        if self.x > 0 and self.y > 0:
            self.childs.append(Dot(self.x - 1, self.y - 1, self.image))
        if self.y > 0:
            self.childs.append(Dot(self.x, self.y - 1, self.image))
        if self.x < width - 1 and self.y > 0:
            self.childs.append(Dot(self.x + 1, self.y - 1, self.image))
        if self.x > 0:
            self.childs.append(Dot(self.x - 1, self.y, self.image))
        if self.x < width - 1:
            self.childs.append(Dot(self.x + 1, self.y, self.image))
        if self.x > 0 and self.y < height - 1:
            self.childs.append(Dot(self.x - 1, self.y + 1, self.image))
        if self.y < height - 1:
            self.childs.append(Dot(self.x, self.y + 1, self.image))
        if self.x < width - 1 and self.y < height - 1:
            self.childs.append(Dot(self.x + 1, self.y + 1, self.image))


    def setDotName(self, name):
        self.name = name

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setCoordinates(self, x, y):
        self.setX(x)
        self.setY(y)
