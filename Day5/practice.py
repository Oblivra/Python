# n = int(input("Enter a number: "))

# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")





# L = ["Harry","Soham","Sachin","Rahul"]

# for name in L:
#     if(name.startswith("S")):
#         print(f"Hello {name}")










# n = int(input("Enter a number: "))

# for i in range(2,n):
#     if(n%i) == 0:
#         print("number is not prime")
#         break
# else:
#     print("numebr is Prime")













# n = int(input("Enter a number: "))
# i = 1
# sum = 0

# while(i<=n):
#     sum += i
#     i += 1
# print(sum)

















# n = int(input("Enter a number: "))
# product = 1

# for i in range(1, n+1):
#     product = product * i
# print(f"factorial is {product}")










'''
for n = 3 print
  *
 ***
*****

'''
# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     print("*"*(2*i-1))








'''
*
**
***
'''

# for i in range(1,4):
#     print("*" * i)










'''
***
* *
***
'''

n = int(input("Enter a number: "))
for i in range(1, n+1):
    if(i==1 or i==n): 
      print("*"*n)
    else:
      print("*" + (" " * (n-2)) + "*")









