# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 23:58:33 2021

@author: Sushovan Chaudhury 2020MT13248
"""    
print("La Yang Li Algorithm Implementation and Correctness")
print("----------------------------------------------")
print("Assumptions")
print("----------------------------------------------")
print("1.The system can handle at most 5 processes/sites,Increasing the number of processes complicate the data structures being used")
print("2.Any messages in transit should be handled during program input")
print("3.Messages being sent between two consecutive timestamps are assumed to be sent in the next higher timestamp as per convention")
print("4.The algorithm is primarily for NON-FIFO and causal ordering of messages are not maintained,however irrespective of FIFO and NON-FIFO Communication channel,it works because such complexities are handled in input")
print("5.The program only deals with white messages as they are used to calculate channel states locally")
print("6.Messages in transit are calculated in channel states within the program")
print("7.White messages received after the first snapshot are ignored")
print("8.The program can accomodate a single snapshot at a time and check for consistency.If snapshot is taken again, rerun the program and reset all messages as white")
print("9.Program successfully checks if the snapshot being taken is consistent or not")
print("10.The programmer assumes that for better clarity the end user has a logical State-Time diagram of the problem handy to compare results")
print("For the logic behind implementation kindly follow the read me file")
print("-------------------------------------------------------")
p=int(input("Enter maximum number of process in the system as 5"))
p1=int(input("Enter relevant number of processes"))
c1=p1*(p1-1)
c=p*(p-1)
print("number of max processes",p)
print("number of max channels",c)
print("number of relevant processes",p1)
print("Number of relevant channels",c1)

    
p1sentlist=[]
p2sentlist=[]
p3sentlist=[]
p4sentlist=[]
p5sentlist=[]
p1recplist=[]
p2recplist=[]
p3recplist=[] 
p4recplist=[]
p5recplist=[]
ts1=int(input("Enter total num of timestamps"))
print("Please enter history of white processes preferably(not mandatory) till",ts1,"th sec")
for i in range(ts1):
 print("Timestamp t",i+1,"[please provide cummulative send or receipt at a given time stamp ;Include history of previous TS along with current TS when asked for]")
 print("------------------------------------------------------------------------")
 print("Put 0 for values which are not applicable")
 print("For input values see read me file or prepare your own input as per instruction in read me file")
 c12s=int(input("Enter amount sent by p1 to p2 at given timestamp"))
 p1sentlist.append(c12s)
 c13s=int(input("Enter amount sent by p1 to p3 at given timestamp"))
 p1sentlist.append(c13s)
 c14s=int(input("Enter amount sent by p1 to p4 at given timestamp"))
 p1sentlist.append(c14s)
 c15s=int(input("Enter amount sent by p1 to p5 at given timestamp"))
 p1sentlist.append(c15s)
 c21s=int(input("Enter amount sent by p2 to p1 at given timestamp"))
 p2sentlist.append(c21s)
 c23s=int(input("Enter amount sent by p2 to p3 at given timestamp"))
 p2sentlist.append(c23s)
 c24s=int(input("Enter amount sent by p2 to p4 at given timestamp"))
 p2sentlist.append(c24s)
 c25s=int(input("Enter amount sent by p2 to p5 at given timestamp"))
 p2sentlist.append(c25s)
 c31s=int(input("Enter amount sent by p3 to p1 at given timestamp"))
 p3sentlist.append(c31s)
 c32s=int(input("Enter amount sent by p3 to p2 at given timestamp"))
 p3sentlist.append(c32s)
 c34s=int(input("Enter amount sent by p3 to p4 at given timestamp"))
 p3sentlist.append(c34s)
 c35s=int(input("Enter amount sent by p3 to p5 at given timestamp"))
 p3sentlist.append(c35s)
 c41s=int(input("Enter amount sent by p4 to p1 at given timestamp"))
 p4sentlist.append(c41s)
 c42s=int(input("Enter amount sent by p4 to p2 at given timestamp"))
 p4sentlist.append(c42s)
 c43s=int(input("Enter amount sent by p4 to p3 at given timestamp"))
 p4sentlist.append(c43s)
 c45s=int(input("Enter amount sent by p4 to p5 at given timestamp"))
 p4sentlist.append(c45s)
 c51s=int(input("Enter amount sent by p5 to p1 at given timestamp"))
 p5sentlist.append(c51s)
 c52s=int(input("Enter amount sent by p5 to p2 at given timestamp"))
 p5sentlist.append(c52s)
 c53s=int(input("Enter amount sent by p5 to p3 at given timestamp"))
 p5sentlist.append(c53s)
 c54s=int(input("Enter amount sent by p5 to p4 at given timestamp"))
 p5sentlist.append(c54s)
 c21r=int(input("Enter amount received by p1 from p2 at given timestamp"))
 p1recplist.append(c21r)
 c31r=int(input("Enter amount received by p1 from p3 at given timestamp"))
 p1recplist.append(c31r)
 c41r=int(input("Enter amount received by p1 from p4 at given timestamp"))
 p1recplist.append(c41r)
 c51r=int(input("Enter amount received by p1 from p5 at given timestamp"))
 p1recplist.append(c51r)
 c12r=int(input("Enter amount received by p2 from p1 at given timestamp"))
 p2recplist.append(c12r)
 c32r=int(input("Enter amount received by p2 from p3 at given timestamp"))
 p2recplist.append(c32r)
 c42r=int(input("Enter amount received by p2 from p4 at given timestamp"))
 p2recplist.append(c42r)
 c52r=int(input("Enter amount received by p2 from p5 at given timestamp"))
 p2recplist.append(c52r)
 c13r=int(input("Enter amount received by p3 from p1 at given timestamp"))
 p3recplist.append(c13r)
 c23r=int(input("Enter amount received by p3 from p2 at given timestamp"))
 p3recplist.append(c23r)
 c43r=int(input("Enter amount received by p3 from p4 at given timestamp"))
 p3recplist.append(c43r)
 c53r=int(input("Enter amount received by p3 from p5 at given timestamp"))
 p3recplist.append(c53r)
 c14r=int(input("Enter amount received by p4 from p1 at given timestamp"))
 p4recplist.append(c14r)
 c24r=int(input("Enter amount received by p4 from p2 at given timestamp"))
 p4recplist.append(c24r)
 c34r=int(input("Enter amount received by p4 from p3 at given timestamp"))
 p4recplist.append(c34r)
 c54r=int(input("Enter amount received by p4 from p5 at given timestamp"))
 p4recplist.append(c54r)
 c15r=int(input("Enter amount received by p5 from p1 at given timestamp"))
 p5recplist.append(c15r)
 c25r=int(input("Enter amount received by p5 from p2 at given timestamp"))
 p5recplist.append(c25r)
 c35r=int(input("Enter amount received by p5 from p3 at given timestamp"))
 p5recplist.append(c35r)
 c45r=int(input("Enter amount received by p5 from p4 at given timestamp"))
 p5recplist.append(c45r)
print(p1sentlist)
print(p2sentlist)
print(p3sentlist)
print(p4sentlist)
print(p5sentlist)
print(p1recplist)
print(p2recplist)
print(p3recplist)
print(p4recplist)
print(p5recplist)
def driver_code():
    X=int(input("Enter value for X"))
    Y=int(input("Enter value for Y"))
    Z=int(input("Enter value for Z"))
    P=int(input("Enter value for P"))
    Q=int(input("Enter value for Q"))
    ts=int(input("Enter the time stamp where snap shot is to be taken"))
    print("All WHITE MESSAGES RECEIVED BEFORE ",ts,"th sec ARE RECORDED")
    print("PROCESSES TURN RED AFTER TAKING SNAPSHOT")
    print("PROCESSES AFTER",ts,"th sec ARE STILL WHITE AND TURN RED AFTER NEXT SNAPSHOT")
    print("MESSAGES RECEIVED AFTER ",ts,"th sec ARE STILL WHITE AND TURN RED AFTER NEXT SNAPSHOT")
    totalp1sent=p1sentlist[(ts-1)*(p-1)]+p1sentlist[(ts-1)*(p-1)+1]+p1sentlist[(ts-1)*(p-1)+2]+p1sentlist[(ts-1)*(p-1)+3]
    totalp2sent=p2sentlist[(ts-1)*(p-1)]+p2sentlist[(ts-1)*(p-1)+1]+p2sentlist[(ts-1)*(p-1)+2]+p2sentlist[(ts-1)*(p-1)+3]
    totalp3sent=p3sentlist[(ts-1)*(p-1)]+p3sentlist[(ts-1)*(p-1)+1]+p3sentlist[(ts-1)*(p-1)+2]+p3sentlist[(ts-1)*(p-1)+3]
    totalp4sent=p4sentlist[(ts-1)*(p-1)]+p4sentlist[(ts-1)*(p-1)+1]+p4sentlist[(ts-1)*(p-1)+2]+p4sentlist[(ts-1)*(p-1)+3]
    totalp5sent=p5sentlist[(ts-1)*(p-1)]+p5sentlist[(ts-1)*(p-1)+1]+p5sentlist[(ts-1)*(p-1)+2]+p5sentlist[(ts-1)*(p-1)+3]
    totalp1recp=p1recplist[(ts-1)*(p-1)]+p1recplist[(ts-1)*(p-1)+1]+p1recplist[(ts-1)*(p-1)+2]+p1recplist[(ts-1)*(p-1)+3]
    totalp2recp=p2recplist[(ts-1)*(p-1)]+p2recplist[(ts-1)*(p-1)+1]+p2recplist[(ts-1)*(p-1)+2]+p2recplist[(ts-1)*(p-1)+3]
    totalp3recp=p3recplist[(ts-1)*(p-1)]+p3recplist[(ts-1)*(p-1)+1]+p3recplist[(ts-1)*(p-1)+2]+p3recplist[(ts-1)*(p-1)+3]
    totalp4recp=p4recplist[(ts-1)*(p-1)]+p4recplist[(ts-1)*(p-1)+1]+p4recplist[(ts-1)*(p-1)+2]+p4recplist[(ts-1)*(p-1)+3]
    totalp5recp=p5recplist[(ts-1)*(p-1)]+p5recplist[(ts-1)*(p-1)+1]+p5recplist[(ts-1)*(p-1)+2]+p5recplist[(ts-1)*(p-1)+3]
    XC=X+totalp1recp-totalp1sent
    YC=Y+totalp2recp-totalp2sent
    ZC=Z+totalp3recp-totalp3sent
    PC=P+totalp4recp-totalp4sent
    QC=Q+totalp5recp-totalp5sent
    

    c12=p1sentlist[(ts-1)*(p-1)]-p2recplist[(ts-1)*(p-1)]
    print("Value of C12:",c12)
    c13=p1sentlist[(ts-1)*(p-1)+1]-p3recplist[(ts-1)*(p-1)]
    print("Value of C13:",c13)
    c14=p1sentlist[(ts-1)*(p-1)+2]-p4recplist[(ts-1)*(p-1)]
    print("Value of C14:",c14)
    c15=p1sentlist[(ts-1)*(p-1)+3]-p5recplist[(ts-1)*(p-1)]
    print("Value of C15:",c15)
    c21=p2sentlist[(ts-1)*(p-1)]-p1recplist[(ts-1)*(p-1)]
    print("Value of C21:",c21)
    c23=p2sentlist[(ts-1)*(p-1)+1]-p3recplist[(ts-1)*(p-1)+1]
    print("Value of C23:",c23)
    c24=p2sentlist[(ts-1)*(p-1)+2]-p4recplist[(ts-1)*(p-1)+1]
    print("Value of C24:",c24)
    c25=p2sentlist[(ts-1)*(p-1)+3]-p5recplist[(ts-1)*(p-1)+1]
    print("Value of C25:",c25)
    c31=p3sentlist[(ts-1)*(p-1)]-p1recplist[(ts-1)*(p-1)+1]
    print("Value of C31:",c31)
    c32=p3sentlist[(ts-1)*(p-1)+1]-p2recplist[(ts-1)*(p-1)+1]
    print("Value of C32:",c32)
    c34=p3sentlist[(ts-1)*(p-1)+2]-p4recplist[(ts-1)*(p-1)+2]
    print("Value of C34:",c34)
    c35=p3sentlist[(ts-1)*(p-1)+3]-p5recplist[(ts-1)*(p-1)+2]
    print("Value of C35:",c35)
    c41=p4sentlist[(ts-1)*(p-1)]-p1recplist[(ts-1)*(p-1)+2]
    print("Value of C41:",c41)
    c42=p4sentlist[(ts-1)*(p-1)+1]-p2recplist[(ts-1)*(p-1)+2]
    print("Value of C42:",c42)
    c43=p4sentlist[(ts-1)*(p-1)+2]-p3recplist[(ts-1)*(p-1)+2]
    print("Value of C43:",c43)
    c45=p4sentlist[(ts-1)*(p-1)+3]-p5recplist[(ts-1)*(p-1)+3]
    print("Value of C45:",c45)
    c51=p5sentlist[(ts-1)*(p-1)]-p1recplist[(ts-1)*(p-1)+3]
    print("Value of C51:",c51)
    c52=p5sentlist[(ts-1)*(p-1)+1]-p2recplist[(ts-1)*(p-1)+3]
    print("Value of C52:",c52)
    c53=p5sentlist[(ts-1)*(p-1)+2]-p3recplist[(ts-1)*(p-1)+3]
    print("Value of C53:",c53)
    c54=p5sentlist[(ts-1)*(p-1)+3]-p4recplist[(ts-1)*(p-1)+3]
    print("Value of C54:",c54)
    print("----Value of X,Y,Z,P and Q at the time of snapshot------------")
    print("Current value of X is:",XC)
    print("Current value of Y is:",YC)
    print("Current value of Z is:",ZC)
    print("Current value of P is:",PC)
    print("Current value of Q is:",QC)
    Total_Value=XC+YC+ZC+PC+QC+c12+c13+c14+c15+c23+c21+c24+c25+c31+c32+c34+c35+c41+c42+c43+c45+c51+c52+c53+c54
    Initial_Money=X+Y+Z+P+Q
    print("Initial money in the system:",Initial_Money)
    print("Total money in the system after snapshot at",ts,"th sec is:",Total_Value)
    def IsConsistent():

        if(Total_Value==Initial_Money):

            print("Consistent Global State Recorded,Amount Preserved in system")

        else:

            print("State is Inconsistent,Local and Global snapshots mismatch")
    IsConsistent()
driver_code()
answer=str(input("You want to take another snap shot?Type Y or N"))
if(answer=='Y'):
    driver_code() 
else:
    print("Thank You")






 