#File for micro:bit
from microbit import *
import random
display.clear()
Lpattern=[9,6,3]
GO=Lpattern+[0]*8 #For making pattern`s tail looks like '00000'
print("START") #To make sure running
while True:
    Dwe=random.sample([0,1,2,3,4],2)
    for i in range(len(GO)):
        for j in range(i,-1,-1): #If you put increasing direction. it shapes akward
            k0=Dwe[0]
            k1=Dwe[1]
            if j<=4: 
                display.set_pixel(k0,j,GO[(i-j)%len(GO)]) #First 'rain'               
            if 2<j<8:
                display.set_pixel(k1,(j-3),GO[(i-j)%len(GO)]) #Second 'rain'
            sleep(20)
