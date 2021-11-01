import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for colour, nos in kwargs.items():
            self.contents += [colour]*nos

    def draw(self, nos):
        lst = []
        if nos < len(self.contents):
            for _ in range(nos):
                index = random.randrange(len(self.contents))
                lst.append(self.contents[index])
                self.contents.pop(index)
            '''
            lst = random.sample(self.contents, nos)
            for item in lst:
                self.contents.remove(item)
            '''
        else:
            lst = self.contents.copy()
            self.contents = []
        return lst


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    exp_balls = []
    correct = 0
    for name, num in expected_balls.items():
        exp_balls += [name]*num
    for _ in range(num_experiments):
        h = copy.deepcopy(hat)
        drawn_balls = h.draw(num_balls_drawn)
        balls_req = sum([1 for k, v in expected_balls.items()
                        if drawn_balls.count(k) >= v])
        correct += 1 if balls_req == len(expected_balls) else 0

    return correct/num_experiments
