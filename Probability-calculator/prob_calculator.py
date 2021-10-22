import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for colour, nos in kwargs.items():
            self.contents += [colour]*nos


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


# Testing
h = Hat(Red=1, blue=3)
print(h.contents)
