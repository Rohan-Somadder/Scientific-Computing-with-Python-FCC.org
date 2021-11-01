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
            #ṇself.contents = []
        return lst


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    exp_balls = []
    correct = 0
    for name, num in expected_balls.items():
        exp_balls += [name]*num
    exp_balls.sort()
    for _ in range(num_experiments):
        h = copy.deepcopy(hat)
        drawn_balls = h.draw(num_balls_drawn)
        drawn_balls.sort()
        # checking is correcting extra situations --- do a presciese match
        balls_req = sum([1 for k, v in expected_balls.items() if drawn_balls.count(k) >= v])
        correct += 1 if balls_req == len(expected_balls) else 0
        '''
        if len(drawn_balls) == len(exp_balls):
            result = (drawn_balls == exp_balls)
        else:
            result = all([(ele in exp_balls) for ele in drawn_balls]) if (len(drawn_balls) > len(
                exp_balls)) else all([(ele in drawn_balls) for ele in exp_balls])
        if result:
            correct += 1
        '''
    return correct/num_experiments


# Testing
# '''
random.seed(95)
h_ = Hat(blue=3, red=2, green=6)
print(h_.contents)
print(experiment(h_, {"blue": 2, "green": 1}, 4, 1000))
# '''
