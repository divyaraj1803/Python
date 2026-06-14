n=int(input("enter a number:"))

# for i in range(1,n+1):
#     print("*"*(n-i)," "*(2*i+1),"*"*(n-i))
#     print("")
for i in range(0,n):
    print((n-i)*"*",end="")
    print((2*i+1)*" ",end="")
    print((n-i)*"*",end="")
    print()



for i in range(0,n+1):
    print("*"*i,end="")
    print((2*(n-i)+1)*" ",end="")
    print("*"*i,end="")
    print()
    