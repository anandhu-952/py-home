s = int(input("enter first year:"))
e = int(input("enter second year:"))
if(s<e):
    print("leap years are:")
    for i in range(s,e):
        if(i%4==0 and i%100!=0):
            print(i,end="")
            print()
        else:
            print("invalid")
