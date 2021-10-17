class Rectangle:
    def __init__(self, w, h):
        self.height = h
        self.width = w

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_height(self, h):
        self.height = h

    def set_width(self, w):
        self.width = w

    def get_area(self):
        return (self.height*self.width)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        pic = ('*'*self.width + '\n')*self.height
        return pic

    def get_amount_inside(self, shape):
        return self.get_area()//shape.get_area()


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a,a)

    def __str__(self):
        return f"Square(side={self.height})"

    def set_side(self, a):
        self.height = a
        self.width = a

    def set_width(self, w):
        self.set_side(w)

    def set_height(self, h):
        self.set_side(h)
