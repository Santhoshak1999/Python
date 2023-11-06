#Write a Python program that accepts a filename from the user and prints the extension of the file.
#Sample filename : abc.java

filename = input("Enter the File Name: ")
fextension = filename.split(".")
print("The extension of the file is: ", repr(fextension[-1]))