# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
f=open("database.txt","a")
while(True):
    #input
    
    name=input("Enter name :")
    number=input("Enter phone Number :")
    place=input("Enter the place : ")
    temp=input("Enter the body temperature:")
    
    #write into the file
    print(name,end=',',file=f)
    print(number,end=',',file=f)
    print(place,end=',',file=f)
    print(temp,end='\n',file=f)
    print("Data saved successfully")
    #next input
    choice=input("Y for next input ,else any other char")
    if(choice.upper()=='Y'):
        pass
    else:
        break

f.close()
f=open("database.txt","r")
data=f.readlines()
#display data

for instance in data :
    print(instance)
        
f.close()