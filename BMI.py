#formula to calculate body mass index
#BMI = wieght / (hight * hieght)

w = float(input("enter wieght in kg: "))
h = float(input("enter your height in meter"))
BMI = w / h ** 2
print(f"Your Body Mass Index is: {BMI}")