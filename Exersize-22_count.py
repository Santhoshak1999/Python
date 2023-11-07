# list = [1,4,2,4,6,7,4,9,6,0,1,8,4,9,5,8,3,4,4,4,4]
# print(list.count(4))

def list_count_4(list):
    count = 0
    for i in list:
        if i == 4:
            count+=1
    return count

list = []
n = int(input("Enter how many item you want to insert: "))
for i in range(n):
    x = int(input(f"Enter element {i}: "))
    list.append(x)

print("The no.of 4 in the list is:", list_count_4(list))

