"""
NAME: Christopher McGrath
DATE: 1/16/20
DESC: Determining if a number is prime in python
"""

num = int(input("Enter your number:"))
count = 0

for i in range(2,num-1):
    if num % i == 0:
        print("Number is not prime")
        count = 1
        break
    
if count != 1:
    print("Number is prime")
    