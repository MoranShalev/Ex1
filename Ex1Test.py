import unittest
from Building import Building
from CallForElevator import CallForElevator
from Elev import Elev
from Main import csvToCallList


class MyTestCase(unittest.TestCase):
    def test_Building(self):
        b1 = Building("B1.json")
        self.assertEqual(-2, b1.minFloor)
        b2 = Building("B2.json")
        self.assertEqual(2, b2.numOfElevators)
        b3 = Building("B3.json")
        self.assertEqual(3.0, b3.getElev(0).speed)
        b4 = Building("B4.json")
        self.assertEqual(1.6666666666666667, b4.getElev(3).timeForClose)
        b5 = Building("B5.json")
        elev2 = {'_id': 2, '_speed': 5.0, '_minFloor': -10, '_maxFloor': 100, '_closeTime': 2.0, '_openTime': 2.0,
                 '_startTime': 3.0, '_stopTime': 3.0}
        self.assertEqual(elev2, b5.elevators[2])

    def test_CallForElevator(self):
        callList1 = csvToCallList("Calls_a.csv")
        for i in callList1:
            c1 = i.src
        self.assertEqual('7', c1)
        callList2 = csvToCallList("Calls_b.csv")
        for i in callList2:
            c2 = i.ElevState
        self.assertEqual('0', c2)
        callList3 = csvToCallList("Calls_c.csv")
        for i in callList3:
            c3 = i.dest
        self.assertEqual('69', c3)
        callList4 = csvToCallList("Calls_d.csv")
        for i in callList4:
            c4 = i.time
        self.assertEqual('3599.437366', c4)


if __name__ == '__main__':
    unittest.main()
