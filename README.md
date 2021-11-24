# Ex1 - OOP COURSE 


## Elevator problem - offline algorithm

In this task the challenge will focus on the offline version of the smart elevator problem that we encounter in the first task - meaning all the readings are given to us in advance, and we are only required to embed each reading in a benevolent manner (so that the rule of waiting for elevators is reduced to a minimum). 
In fact, the current task focuses mainly on the challenge of assigning a "call" to the elevator.

### literature Review:
https://paradigm.suss.edu.sg/the-smart-elevator-scheduling-algorithm-an-illustration-of-computational-intelligence/
http://www.intertent.co.il/2011/07/elevator-algorithm.html
http://www.csunplugged.org.il/lessons/disk-scheduling/


### how are Algorithem actully works: 
First the algorithm read the files. Then go through each call in the reading file and look for the elevator that can get to it in the fastest time (just if the elevator and the call are in the same direction of course) based on the lists of that elevator.
After adding the call to the elevator calls list, and then update the current floor.
we initialize the flag with true and continue to update the flag according to the elevator's progress in its calls list.


### primary functions in this code:
getElev- this function return the elevator object with the input id.

elevPos- this function return the position of elevator at the moment.

csvToCallList- this function read a csv file to our project object CallForElevator.

offlineAlgo- our main function. gets csv file and json file as input and running all the proccess to get the new csv file as putput with the wanted results.

theFastElev- using a loop to check which elevator has the fastest way to reach our call consider the elevator calls list.

totalTimeForCall- this function find the elevators time to reach a call. this calculate helps us to find the fastest elevator for a call.




## UML of our project:
![UML](https://user-images.githubusercontent.com/94013553/143307348-3dbbb562-1ba5-4314-b5c8-c839e477654a.png)

## Our results:
![RrESULTS](https://user-images.githubusercontent.com/94013553/143307556-19b6a7f1-a4b3-46e8-bb3e-f57bebf7de49.png)
