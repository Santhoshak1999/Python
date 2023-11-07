text = input("Enter a String: ")
n = int(input("Enter how many no.of times you want: "))
# print(text * 3)
#Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
def larger_string(text, n):
    print(text * n)

larger_string(text, n)