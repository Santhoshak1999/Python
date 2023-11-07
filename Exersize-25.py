"""
#Solution-1
def is_group_member(group_data, n):
   # return n in group_data

group = [1,5,2,9,5,0,2,3]
member1 = 4
member2 = 2
print(is_group_member(group, member))
print(is_group_member(group, 2))

"""
#Solution-2
def is_group_member(group_data, n):
    for i in group_data:
        if n == i:
            return True
    return False

group = [2,4,7,4,9,6]
member1 = 2
member2 = 1
print(is_group_member(group, member1))
print(is_group_member(group, member2))



