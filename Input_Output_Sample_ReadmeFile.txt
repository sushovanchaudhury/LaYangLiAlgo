In [3]: runfile('C:/Users/91825/OneDrive/Desktop/DC_Assignment/LiYang.py', wdir='C:/Users/91825/OneDrive/Desktop/DC_Assignment')

La Yang Li Algorithm Implementation and Correctness

----------------------------------------------

Assumptions

----------------------------------------------

1.The system can handle at most 5 processes/sites,Increasing the number of processes complicate the data structures being used

2.Any messages in transit should be handled during program input

3.Messages being sent between two consecutive timestamps are assumed to be sent in the next higher timestamp as per convention

4.The algorithm is primarily for NON-FIFO and causal ordering of messages are not maintained,however irrespective of FIFO and NON-FIFO Communication channel,it works because such complexities are handled in input

5.The program only deals with white messages as they are used to calculate channel states locally

6.Messages in transit are calculated in channel states within the program

7.White messages received after the first snapshot are ignored

8.The program can accomodate a single snapshot at a time and check for consistency.If snapshot is taken again, rerun the program and reset all messages as white

9.Program successfully checks if the snapshot being taken is consistent or not

10.The programmer assumes that for better clarity the end user has a logical State-Time diagram of the problem handy to compare results

For the logic behind implementation kindly follow the read me file

-------------------------------------------------------



Enter maximum number of process in the system as 5 5



Enter relevant number of processes 3

number of max processes 5

number of max channels 20

number of relevant processes 3

Number of relevant channels 6



Enter total num of timestamps 5

Please enter history of white processes preferably(not mandatory) till 5 th sec

Timestamp t 1 [please provide cummulative send or receipt at a given time stamp ;Include history of previous TS along with current TS when asked for]

------------------------------------------------------------------------

Put 0 for values which are not applicable

For input values see read me file or prepare your own input as per instruction in read me file



Enter amount sent by p1 to p2 at given timestamp 10



Enter amount sent by p1 to p3 at given timestamp0



Enter amount sent by p1 to p4 at given timestamp0



Enter amount sent by p1 to p5 at given timestamp0



Enter amount sent by p2 to p1 at given timestamp0



Enter amount sent by p2 to p3 at given timestamp0



Enter amount sent by p2 to p4 at given timestamp0



Enter amount sent by p2 to p5 at given timestamp0



Enter amount sent by p3 to p1 at given timestamp0



Enter amount sent by p3 to p2 at given timestamp0



Enter amount sent by p3 to p4 at given timestamp0



Enter amount sent by p3 to p5 at given timestamp0



Enter amount sent by p4 to p1 at given timestamp0



Enter amount sent by p4 to p2 at given timestamp0



Enter amount sent by p4 to p3 at given timestamp0



Enter amount sent by p4 to p5 at given timestamp0



Enter amount sent by p5 to p1 at given timestamp0



Enter amount sent by p5 to p2 at given timestamp0



Enter amount sent by p5 to p3 at given timestamp0



Enter amount sent by p5 to p4 at given timestamp0



Enter amount received by p1 from p2 at given timestamp0



Enter amount received by p1 from p3 at given timestamp0



Enter amount received by p1 from p4 at given timestamp0



Enter amount received by p1 from p5 at given timestamp0



Enter amount received by p2 from p1 at given timestamp0



Enter amount received by p2 from p3 at given timestamp0



Enter amount received by p2 from p4 at given timestamp0



Enter amount received by p2 from p5 at given timestamp0



Enter amount received by p3 from p1 at given timestamp0



Enter amount received by p3 from p2 at given timestamp0



Enter amount received by p3 from p4 at given timestamp0



Enter amount received by p3 from p5 at given timestamp0



Enter amount received by p4 from p1 at given timestamp0



Enter amount received by p4 from p2 at given timestamp0



Enter amount received by p4 from p3 at given timestamp0



Enter amount received by p4 from p5 at given timestamp0



Enter amount received by p5 from p1 at given timestamp0



Enter amount received by p5 from p2 at given timestamp0



Enter amount received by p5 from p3 at given timestamp0



Enter amount received by p5 from p4 at given timestamp0

Timestamp t 2 [please provide cummulative send or receipt at a given time stamp ;Include history of previous TS along with current TS when asked for]

------------------------------------------------------------------------

Put 0 for values which are not applicable

For input values see read me file or prepare your own input as per instruction in read me file



Enter amount sent by p1 to p2 at given timestamp10



Enter amount sent by p1 to p3 at given timestamp30



Enter amount sent by p1 to p4 at given timestamp0



Enter amount sent by p1 to p5 at given timestamp0



Enter amount sent by p2 to p1 at given timestamp15



Enter amount sent by p2 to p3 at given timestamp10



Enter amount sent by p2 to p4 at given timestamp0



Enter amount sent by p2 to p5 at given timestamp0



Enter amount sent by p3 to p1 at given timestamp20



Enter amount sent by p3 to p2 at given timestamp0



Enter amount sent by p3 to p4 at given timestamp0



Enter amount sent by p3 to p5 at given timestamp0



Enter amount sent by p4 to p1 at given timestamp0



Enter amount sent by p4 to p2 at given timestamp0



Enter amount sent by p4 to p3 at given timestamp0



Enter amount sent by p4 to p5 at given timestamp0



Enter amount sent by p5 to p1 at given timestamp0



Enter amount sent by p5 to p2 at given timestamp0



Enter amount sent by p5 to p3 at given timestamp0



Enter amount sent by p5 to p4 at given timestamp0



Enter amount received by p1 from p2 at given timestamp0



Enter amount received by p1 from p3 at given timestamp0



Enter amount received by p1 from p4 at given timestamp0



Enter amount received by p1 from p5 at given timestamp0



Enter amount received by p2 from p1 at given timestamp10



Enter amount received by p2 from p3 at given timestamp0



Enter amount received by p2 from p4 at given timestamp0



Enter amount received by p2 from p5 at given timestamp0



Enter amount received by p3 from p1 at given timestamp0



Enter amount received by p3 from p2 at given timestamp0



Enter amount received by p3 from p4 at given timestamp0



Enter amount received by p3 from p5 at given timestamp0



Enter amount received by p4 from p1 at given timestamp0



Enter amount received by p4 from p2 at given timestamp0



Enter amount received by p4 from p3 at given timestamp0



Enter amount received by p4 from p5 at given timestamp0



Enter amount received by p5 from p1 at given timestamp0



Enter amount received by p5 from p2 at given timestamp0



Enter amount received by p5 from p3 at given timestamp0



Enter amount received by p5 from p4 at given timestamp0

Timestamp t 3 [please provide cummulative send or receipt at a given time stamp ;Include history of previous TS along with current TS when asked for]

------------------------------------------------------------------------

Put 0 for values which are not applicable

For input values see read me file or prepare your own input as per instruction in read me file



Enter amount sent by p1 to p2 at given timestamp10



Enter amount sent by p1 to p3 at given timestamp30



Enter amount sent by p1 to p4 at given timestamp0



Enter amount sent by p1 to p5 at given timestamp0



Enter amount sent by p2 to p1 at given timestamp15



Enter amount sent by p2 to p3 at given timestamp10



Enter amount sent by p2 to p4 at given timestamp0



Enter amount sent by p2 to p5 at given timestamp0



Enter amount sent by p3 to p1 at given timestamp20



Enter amount sent by p3 to p2 at given timestamp0



Enter amount sent by p3 to p4 at given timestamp0



Enter amount sent by p3 to p5 at given timestamp0



Enter amount sent by p4 to p1 at given timestamp0



Enter amount sent by p4 to p2 at given timestamp0



Enter amount sent by p4 to p3 at given timestamp0



Enter amount sent by p4 to p5 at given timestamp0



Enter amount sent by p5 to p1 at given timestamp0



Enter amount sent by p5 to p2 at given timestamp0



Enter amount sent by p5 to p3 at given timestamp0



Enter amount sent by p5 to p4 at given timestamp0



Enter amount received by p1 from p2 at given timestamp15



Enter amount received by p1 from p3 at given timestamp0



Enter amount received by p1 from p4 at given timestamp0



Enter amount received by p1 from p5 at given timestamp0



Enter amount received by p2 from p1 at given timestamp10



Enter amount received by p2 from p3 at given timestamp0



Enter amount received by p2 from p4 at given timestamp0



Enter amount received by p2 from p5 at given timestamp0



Enter amount received by p3 from p1 at given timestamp0



Enter amount received by p3 from p2 at given timestamp10



Enter amount received by p3 from p4 at given timestamp0



Enter amount received by p3 from p5 at given timestamp0



Enter amount received by p4 from p1 at given timestamp0



Enter amount received by p4 from p2 at given timestamp0



Enter amount received by p4 from p3 at given timestamp0



Enter amount received by p4 from p5 at given timestamp0



Enter amount received by p5 from p1 at given timestamp0



Enter amount received by p5 from p2 at given timestamp0



Enter amount received by p5 from p3 at given timestamp0



Enter amount received by p5 from p4 at given timestamp0

Timestamp t 4 [please provide cummulative send or receipt at a given time stamp ;Include history of previous TS along with current TS when asked for]

------------------------------------------------------------------------

Put 0 for values which are not applicable

For input values see read me file or prepare your own input as per instruction in read me file



Enter amount sent by p1 to p2 at given timestamp10



Enter amount sent by p1 to p3 at given timestamp30



Enter amount sent by p1 to p4 at given timestamp0



Enter amount sent by p1 to p5 at given timestamp0



Enter amount sent by p2 to p1 at given timestamp15



Enter amount sent by p2 to p3 at given timestamp10



Enter amount sent by p2 to p4 at given timestamp0



Enter amount sent by p2 to p5 at given timestamp0



Enter amount sent by p3 to p1 at given timestamp20



Enter amount sent by p3 to p2 at given timestamp0



Enter amount sent by p3 to p4 at given timestamp0



Enter amount sent by p3 to p5 at given timestamp0



Enter amount sent by p4 to p1 at given timestamp0



Enter amount sent by p4 to p2 at given timestamp0



Enter amount sent by p4 to p3 at given timestamp0



Enter amount sent by p4 to p5 at given timestamp0



Enter amount sent by p5 to p1 at given timestamp0



Enter amount sent by p5 to p2 at given timestamp0



Enter amount sent by p5 to p3 at given timestamp0



Enter amount sent by p5 to p4 at given timestamp0



Enter amount received by p1 from p2 at given timestamp15



Enter amount received by p1 from p3 at given timestamp20



Enter amount received by p1 from p4 at given timestamp0



Enter amount received by p1 from p5 at given timestamp0



Enter amount received by p2 from p1 at given timestamp10



Enter amount received by p2 from p3 at given timestamp0



Enter amount received by p2 from p4 at given timestamp0



Enter amount received by p2 from p5 at given timestamp0



Enter amount received by p3 from p1 at given timestamp30



Enter amount received by p3 from p2 at given timestamp10



Enter amount received by p3 from p4 at given timestamp0



Enter amount received by p3 from p5 at given timestamp0



Enter amount received by p4 from p1 at given timestamp0



Enter amount received by p4 from p2 at given timestamp0



Enter amount received by p4 from p3 at given timestamp0



Enter amount received by p4 from p5 at given timestamp0



Enter amount received by p5 from p1 at given timestamp0



Enter amount received by p5 from p2 at given timestamp0



Enter amount received by p5 from p3 at given timestamp0



Enter amount received by p5 from p4 at given timestamp0

Timestamp t 5 [please provide cummulative send or receipt at a given time stamp ;Include history of previous TS along with current TS when asked for]

------------------------------------------------------------------------

Put 0 for values which are not applicable

For input values see read me file or prepare your own input as per instruction in read me file



Enter amount sent by p1 to p2 at given timestamp10



Enter amount sent by p1 to p3 at given timestamp30



Enter amount sent by p1 to p4 at given timestamp0



Enter amount sent by p1 to p5 at given timestamp0



Enter amount sent by p2 to p1 at given timestamp15



Enter amount sent by p2 to p3 at given timestamp10



Enter amount sent by p2 to p4 at given timestamp0



Enter amount sent by p2 to p5 at given timestamp0



Enter amount sent by p3 to p1 at given timestamp20



Enter amount sent by p3 to p2 at given timestamp0



Enter amount sent by p3 to p4 at given timestamp0



Enter amount sent by p3 to p5 at given timestamp0



Enter amount sent by p4 to p1 at given timestamp0



Enter amount sent by p4 to p2 at given timestamp0



Enter amount sent by p4 to p3 at given timestamp0



Enter amount sent by p4 to p5 at given timestamp0



Enter amount sent by p5 to p1 at given timestamp0



Enter amount sent by p5 to p2 at given timestamp0



Enter amount sent by p5 to p3 at given timestamp0



Enter amount sent by p5 to p4 at given timestamp0



Enter amount received by p1 from p2 at given timestamp15



Enter amount received by p1 from p3 at given timestamp20



Enter amount received by p1 from p4 at given timestamp0



Enter amount received by p1 from p5 at given timestamp0



Enter amount received by p2 from p1 at given timestamp10



Enter amount received by p2 from p3 at given timestamp0



Enter amount received by p2 from p4 at given timestamp0



Enter amount received by p2 from p5 at given timestamp0



Enter amount received by p3 from p1 at given timestamp30



Enter amount received by p3 from p2 at given timestamp10



Enter amount received by p3 from p4 at given timestamp0



Enter amount received by p3 from p5 at given timestamp0



Enter amount received by p4 from p1 at given timestamp0



Enter amount received by p4 from p2 at given timestamp0



Enter amount received by p4 from p3 at given timestamp0



Enter amount received by p4 from p5 at given timestamp0



Enter amount received by p5 from p1 at given timestamp0



Enter amount received by p5 from p2 at given timestamp0



Enter amount received by p5 from p3 at given timestamp0



Enter amount received by p5 from p4 at given timestamp0

[10, 0, 0, 0, 10, 30, 0, 0, 10, 30, 0, 0, 10, 30, 0, 0, 10, 30, 0, 0]

[0, 0, 0, 0, 15, 10, 0, 0, 15, 10, 0, 0, 15, 10, 0, 0, 15, 10, 0, 0]

[0, 0, 0, 0, 20, 0, 0, 0, 20, 0, 0, 0, 20, 0, 0, 0, 20, 0, 0, 0]

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

[0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 15, 20, 0, 0, 15, 20, 0, 0]

[0, 0, 0, 0, 10, 0, 0, 0, 10, 0, 0, 0, 10, 0, 0, 0, 10, 0, 0, 0]

[0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 30, 10, 0, 0, 30, 10, 0, 0]

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



Enter value for X 500



Enter value for Y 400



Enter value for Z 300



Enter value for P 0



Enter value for Q 0



Enter the time stamp where snap shot is to be taken 3

All WHITE MESSAGES RECEIVED BEFORE  3 th sec ARE RECORDED

PROCESSES TURN RED AFTER TAKING SNAPSHOT

PROCESSES AFTER 3 th sec ARE STILL WHITE AND TURN RED AFTER NEXT SNAPSHOT

MESSAGES RECEIVED AFTER  3 th sec ARE STILL WHITE AND TURN RED AFTER NEXT SNAPSHOT

Value of C12: 0

Value of C13: 30

Value of C14: 0

Value of C15: 0

Value of C21: 0

Value of C23: 0

Value of C24: 0

Value of C25: 0

Value of C31: 20

Value of C32: 0

Value of C34: 0

Value of C35: 0

Value of C41: 0

Value of C42: 0

Value of C43: 0

Value of C45: 0

Value of C51: 0

Value of C52: 0

Value of C53: 0

Value of C54: 0

----Value of X,Y,Z,P and Q at the time of snapshot------------

Current value of X is: 475

Current value of Y is: 385

Current value of Z is: 290

Current value of P is: 0

Current value of Q is: 0

Initial money in the system: 1200

Total money in the system after snapshot at 3 th sec is: 1200

Consistent Global State Recorded,Amount Preserved in system



You want to take another snap shot?Type Y or NY



Enter value for X 500



Enter value for Y 400



Enter value for Z 300



Enter value for P 0



Enter value for Q 0



Enter the time stamp where snap shot is to be taken 4

All WHITE MESSAGES RECEIVED BEFORE  4 th sec ARE RECORDED

PROCESSES TURN RED AFTER TAKING SNAPSHOT

PROCESSES AFTER 4 th sec ARE STILL WHITE AND TURN RED AFTER NEXT SNAPSHOT

MESSAGES RECEIVED AFTER  4 th sec ARE STILL WHITE AND TURN RED AFTER NEXT SNAPSHOT

Value of C12: 0

Value of C13: 0

Value of C14: 0

Value of C15: 0

Value of C21: 0

Value of C23: 0

Value of C24: 0

Value of C25: 0

Value of C31: 0

Value of C32: 0

Value of C34: 0

Value of C35: 0

Value of C41: 0

Value of C42: 0

Value of C43: 0

Value of C45: 0

Value of C51: 0

Value of C52: 0

Value of C53: 0

Value of C54: 0

----Value of X,Y,Z,P and Q at the time of snapshot------------

Current value of X is: 495

Current value of Y is: 385

Current value of Z is: 320

Current value of P is: 0

Current value of Q is: 0

Initial money in the system: 1200

Total money in the system after snapshot at 4 th sec is: 1200

Consistent Global State Recorded,Amount Preserved in system



In [2]: 