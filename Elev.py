class Elev:
    def __init__(self, elev):
        self.id = elev['_id']
        self.speed = elev['_speed']
        self.timeForOpen = elev['_openTime']
        self.timeForClose = elev['_closeTime']
        self.startTime = elev['_startTime']
        self.stopTime = elev['_stopTime']
        self.minFloor = elev['_minFloor']
        self.maxFloor = elev['_maxFloor']
        self.pos = 0
        listOfCall = []
        self.listOfCall = listOfCall
        self.flag = True

    def ElevPos(self, Pos):
        self.pos = Pos
