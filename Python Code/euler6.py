#Project Euler Problem 6
y, sumsquare, squaresum = 0, 0, 0
while y <= 100:
    sumsquare = sumsquare + y ** 2
    squaresum = squaresum + y
    y = y + 1
squaresum = squaresum ** 2
diff = squaresum - sumsquare
print ("Problem 6 Answer : " + str(diff))
