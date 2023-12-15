# https://medium.com/@adinasocaci.simona/python-101-type-error-type-checking-and-type-conversion-mathematical-operations-78a12baf5dc2

print(len("Im santhosha K")) #it will give output of lenth of a given string

#print(len(1234)) #it will give a type error becouce type integer has no lenth

#Type Error
#A TypeError in python occurs when an operation or funtion is performed on an object of an inappropriate type.
#This means the the data type of an object is nor compatible with the operation or funtion being applied.
#Example - attempting to add a string and an integer.

name = input("Enter you name: ")
print("Your name has: " + str(len(name)) + " characters");#here we can not concatinate int and string hence we typecast the lenofname to string
