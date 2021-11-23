import csv


class CallForElevator:

    def __init__(self, call):
        arr = []
        for i in call:
            arr.append(i)
        self.someString = call[0]
        self.time = call[1]
        self.src = call[2]
        self.dest = call[3]
        self.ElevState = call[4]
        self.optElev = call[5]
        if self.src > self.dest:
            self.direction = -1
        else:
            self.direction = 1




