#Write a python program to calculate the sum of three given numbers. if the values are equal, return three times their sum
def sum_trice(x,y,z):

    sum = x + y + z
    if x==y==z:
        sum = sum * 3
    return sum;


print("Enter Three numbers")
x = int(input("Enter number1: "))
y = int(input("Enter number2: "))   
z = int(input("Enter number3: "))

print(sum_trice(x, y, z))