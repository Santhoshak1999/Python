# Write a Python program to test whether a number is within 100 of 1000 or 2000.
def near_thousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <=100))

x = int(input("Enter the Amount to check where it is nearly 1000 or 2000: "))
if (near_thousand(x)):
    print("Yes it is nearly 1000 or 2000")
else:
    print("No it is not nearly 1000 or 2000")

