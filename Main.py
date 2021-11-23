import sys

import Elev
import CallForElevator
from Building import Building
import csv


def csvToCallList(csvFile):
    callList = []
    with open(csvFile, 'r') as csv_file:
        file = csv.reader(csv_file)
        for i in file:
            newCall = CallForElevator.CallForElevator(i)
            callList.append(newCall)
    return callList


def offlineAlgo(Building_json, Calls_csv, Output_csv):
    callList = csvToCallList(Calls_csv)
    building1 = Building(Building_json)
    for i in callList:
        fastesElev = (theFastElev(building1, i))
        fastElev = building1.getElev(fastesElev)
        if len(fastElev.listOfCall) == 0:
            if i.direction == -1:
                fastElev.flag = False
        fastElev.listOfCall.append(i)
        i.optElev = fastElev.id
        fastElev.ElevPos(i.src)
    outList = []
    for call in callList:
        outList.append(call.__dict__.values())
    with open(Output_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(outList)


def theFastElev(building, call: CallForElevator):
    minimum = sys.maxsize
    for elev in building.ElevatorList:
        if int(call.src) <= elev.maxFloor or int(call.src) >= elev.minFloor:
            if len(elev.listOfCall) == 0:
                numberOfFloors = int(elev.pos) - int(call.src)
                absPos = abs(numberOfFloors)
                dis = (elev.speed * absPos) + elev.timeForOpen + elev.timeForClose + elev.startTime + elev.stopTime
                if dis < minimum:
                    minimum = dis
                    fastElev = int(elev.id)
            else:
                if call.direction == 1:
                    if elev.flag is True:
                        dis = totalTimeForCall(elev, call)
                        if dis < minimum:
                            minimum = dis
                            fastElev = int(elev.id)
                elif call.direction == -1:
                    if not elev.flag:
                        dis = totalTimeForCall(elev, call)
                        if dis < minimum:
                            minimum = dis
                            fastElev = int(elev.id)
    print(fastElev)
    return fastElev


def totalTimeForCall(elev: Elev, call: CallForElevator):
    time = 0
    for i in elev.listOfCall:
        numberOfFloors = int(i.src) - int(i.dest)
        absPos = abs(numberOfFloors)
        dis = (elev.speed * absPos) + elev.timeForOpen + elev.timeForClose + elev.startTime + elev.stopTime
        time += dis
    addCallTime = (abs(int(elev.listOfCall[len(elev.listOfCall) - 1].dest)) - int(
        call.src)) * elev.speed + elev.timeForOpen + elev.timeForClose + elev.startTime + elev.stopTime
    time += addCallTime
    return int(time)


class Main:
    pass


myName = Main()
#offlineAlgo("B5.json", "Calls_a.csv", "out.csv")
