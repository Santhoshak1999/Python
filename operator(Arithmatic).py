#Operators in Python
# types
#   Arithmatic Operator - +,-,*,/,//(floar division), % (Modulo operator)
#   Comparision operator
#   Logical Operator
#   Assignment Operator
#   Identity Operator
#   Power Operator  =  **

a = 12
b = 12
c = 12.0
d = 5

#Arithmatic Operation in Python
# as you know +,-,*,/ are same in python also

print(a+b) #int + int = int
print(a+c) #int + float = float
print(a-b) #int - int = int
print(a-c) #int - float = float

print(a * b) #int * int = int
print(a * c) #int * float = float

#In the above operation we saw that 
# arithmatic operation int with int it will give ans as interget only
# But in division int and int will provide the ans as floating point number

# Note: in python divion always give a floating opoint number even numerator and denominator as integer

print("Divsion operator")
print(a/b)
print(a/c)

# If you want to get integer value in division then you will go for 
# floor division
# division that discards the remainder and returns the largest whole number less than or equal to the true quotient.

print("Floor division")
print(a//b)
print(a/d)
print(a//d) #it will discard the remainder

print("Power Operator")
# The power Operator is the double asterisk (**).
# it is raise a number (the base) to a power (the exponent)

print(a**b) #a powerof b it will raise variable a as (the base number) and  variable b as (the exponent)
print(2**3) #2*2*2=8
print(4**2) #4*4=16
print(8**4) #8*8*8*8=4096 
# Associvity of Arithmatic Operator

# PEMDAS - Paranthesis, Exponent, Multiplication, Division, Addsion, Subtraction
#           ( )
#   R<- L   ** 
#   L -> R  *, /, //, %
#   L -> R  +, - 
print("Example for Associvity")
print(5 + 2 * 3 - 1 + 10 / 2 ** 2)
#     5 + 2 * 3 - 1 + 10 / 4
#     5 + 6 - 1 + 10 / 4
#     5 + 6 - 1 +  2.5
#ans  12.5