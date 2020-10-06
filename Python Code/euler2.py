#Project Euler Problem 2
sump2, a, b= 0, 1, 2
c = a+b
mylist = []
mylist.append(2)
while c < 4000000:
    if c % 2 == 0:
        mylist.append(c)
    a = b
    b = c
    c = a + b
for d in mylist:
    sump2 = sump2 + d
print ("Problem 2 Answer : " + str(sump2))
