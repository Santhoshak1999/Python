def even_odd(n):
    if n%2 == 0:
        return "even number"
    else:
        return "odd number"


n = int(input("Enter a number"))
print(f"{n} is {even_odd(n)}")