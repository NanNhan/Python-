i = 1
j = 1
while i<9 and j<9:
    for x in range(1,10):
        for y in range(1,x + 1):
            print(x,"*",y,"=",x*y,end=" ")
        print("")
    break