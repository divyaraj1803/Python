# num = int(input("enter a number:"))

# for i in range(1,1+num):
#     if (i==1) or (i==num):
#         print("*"*num,end=" ")
#     else:
#         print("*" + " "*(num-2) + "*",end=" ")
#     print()


# for i in range(5, 0, -1):
#     print('*',end="")
# print()




# name=input("enter your name:")
# membership_type=input("enter your membership type:")

# if(membership_type == "premium"):
#     print(f"Welcome, {name} (Premium Member)! You are eligible for 10% discount.")
#     item1=int(input("enter the price of 1st item:"))
#     item2=int(input("enter the price of 2nd item:"))
#     item3=int(input("enter the price of 3rd item:"))
#     total=item1+item2+item3
#     print("Total before discount:", total)
#     print("Total after discount:",(total-((10/100)*total)))
#     print("Thank you for shopping with Smart Grocery.")
# elif(membership_type == "regular"):
#     print("Welcome, {name}!")
#     item1=int(input("enter the price of 1st item:"))
#     item2=int(input("enter the price of 2nd item:"))
#     item3=int(input("enter the price of 3rd item:"))  
#     total=item1+item2+item3
#     print("Total bill:", total)  
#     print("Thank you for shopping with Smart Grocery.")




# prime=[]
# for num in range (1,100):
#     for i in range(2,num):
#         if (num % i == 0):
#             break
#     else:
#         prime.append(num)
# for i in prime:
#     if (i % 10 == 3):
#         print(i)




nums = [3, 5, 7, 9, 12, 15, 17]
product = 1
for n in nums:
    if n % 6 == 0:
        break
    elif n % 2 != 0:
        product=product * n
print("Product of odd numbers before first multiple of 6 :", product)
