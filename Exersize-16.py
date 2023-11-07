#Write a python program to calculate the difference between a given number and 17. if the number is greater than 27, return twice the absolute differece.

x = int(input("Enter a number: "))
"""dif = x - 17
if x > 17:
    print(abs(dif * 2))
else:
    print(abs(dif))"""

#Define a function named "differece" that takes an integer parameter "n"
def dif17(n):
    if n> 17:
        return abs((n - 17) * 2)
    else:
        return abs(n - 17)
    
print(dif17(x))