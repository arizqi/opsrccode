#!/usr/bin/python
import random
import math

#create function to perform a 20 step random walk per agent

def agentwalk():
        coords = [(1,0), (0,1), (-1,0), (0,-1)]
        x=0
        y=0
        list1=[]
        list2=[]
        while len(list1)<20:
                dx, dy = coords[random.randint(0,3)]
                x += dx
                y += dy
                list1.append(x)
                list2.append(y)

        zp=zip(list1,list2)
        return zp[-1]

plist=[]

#Get 100 end points of 20 step walk
for j in range(100):

        #run agentwalk() for three agents

        list3=[]
        for i in range(3):
                v=agentwalk()
                list3.append(v)
        plist.append(list3)

#this list containts elements that describe the last points of each agents 20 step walk
print plist,"\n"
list4=plist[-1]


#get tuple components
a1=list4[0][0]
a2=list4[0][1]
b1=list4[1][0]
b2=list4[1][1]
c1=list4[2][0]
c2=list4[2][1]


#create new vectors describing lines that connect triangle
v1=[b1-a1,b2-a2]
v2=[c1-b1,c2-b2]
v3=[c1-a1,c2-a2]

#get length of each line
l1=math.sqrt(v1[0]*v1[0]+v1[1]*v1[1])
l2=math.sqrt(v2[0]*v2[0]+v2[1]*v2[1])
l3=math.sqrt(v3[0]*v3[0]+v3[1]*v3[1])

#perimeter is calculated here
p=l1+l2+l3
print "Expected perimeter is ",p
