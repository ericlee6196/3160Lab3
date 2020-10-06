import math


#Project Euler Problem 1
sump1 = 0
x = 0
while x < 1000:
    if x % 3 == 0 or x % 5 == 0:
        sump1 = sump1 + x
    x = x + 1
print ("Problem 1 Answer : " + str(sump1))

