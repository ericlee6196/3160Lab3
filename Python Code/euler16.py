def splitNum(n):
    list = []
    while n > 0:
        list.insert(0, n % 10)
        n = n // 10
    return list


x = 2 ** 1000
sum = 0
mylist = splitNum(x)
for x in mylist:
    sum = sum + x
print (sum)


