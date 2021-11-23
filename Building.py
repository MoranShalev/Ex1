import Elev
import json


class Building:
    def __init__(self, path):
        with open(path, 'r') as f:
            data = json.load(f)
            self.minFloor = data['_minFloor']
            self.maxFloor = data['_maxFloor']
            self.elevators = data['_elevators']
            elevatorList = []
            for i in data['_elevators']:
                elev = Elev.Elev(i)
                elevatorList.append(elev)
            self.ElevatorList = elevatorList
            self.numOfElevators = len(elevatorList)

    def getElev(self, index: int):
        return self.ElevatorList[index]
