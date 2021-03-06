# List qualities
[1, 2, 3] is not [3, 2, 1]      # Ordered
['cat', 5, (4, 2), 2.5, True]   # Can contain any type of data
[1, 2, 3, 4, 5].append([6])     # Mutable


# Swapping elements in a list
# Can you understand why this is buggy?
def swap_elements_buggy(elem1, elem2):
    temp = elem1
    elem1 = elem2
    elem2 = temp
    

def main():
    my_list = [10, 20, 30]
    swap_elements_buggy(my_list[0], my_list[1])
    print(my_list)      # [10, 20, 30]


# This is not buggy
def swap_elements_working(alist, index1, index2):
    temp = alist[index1]
    alist[index1] = alist[index2]
    alist[index2] = temp


    # Shortcut without use of temp:
    # Either side of equal is actually a tuple, parentheses are optional
    (alist[index1], alist[index2]) = (alist[index2], alist[index1])


# Slicing lists = list[start:end:step]
alist = [2, 3, 5, 7, 11, 13, 17]
alist[2:4]          # Test these in IDLE
>>> alist           # 
alist[2:2]          # 
alist[:8]           # 
alist[3:]           # 
alist[:]            # 
alist[-3:-1]        # 
alist[1:4:-1]       # 
alist[::-1]         # 


# Making a copy
numlist = [1, 2, 3, 4, 5]
list2 = numlist[:]
list2 == numlist            # 
list2 is numlist            # 
list3 = numlist.copy()      # This is the same as numlist[:]
list4 = numlist             # What is this called? Aliasing


# Using for each loop with lists
for elem in alist[1::2]:
    print(elem)


# Looping using index and range
for i in range(1, len(alist), 2):
    print(alist[i])


# To delete use del or remove
num_list = [50, 30, 40, 60, 90, 90]
del num_list[1]         
>>> num_list            # What would return?
del num_list[1:4]
>>> num_list            # What would return?
num_list.remove(90)
>>> num_list            # What would return?


# List functions and review
alist = [6, 3, 12, 4]
len(alist)              # Test these out in IDLE 
alist.reverse()         # 
alist.sort()            # 
sorted = alist.sort()   # 
alist.pop()             # 
alist.pop(2)            # 
alist.append(5)         # 
blist = alist + [22]    # 
alist.extend([4, 2])    # 
alist.insert(3, 50)     # 
alist.remove(50)        # 
alist.count(50)         #


# Passing a list as a parameter/argument
def times_two(alist):
    # Modifies list
    for i in range(len(alist)):
        alist[i] = alist[i] * 2

nums = [1, 2, 3, 4]
print(nums)             # 
times_two(nums)
print(nums)             # 


def times_two_pure(alist):
    # Pure function
    doubled = []
    for item in alist:
        doubled.append(item * 2)
    return doubled              # Have to return the new list

nums2 = [1, 2, 3, 4]
doubled = times_two_pure(nums2)
print(doubled)          # 
print(nums2)            # 


# Intro to comprehension
mylist = [1, 2, 3, 4, 5]

# Creating a list using for loop
squared_for = []
for num in mylist:
    squared_for.append(num ** 2)

# Creating a list using comprehension 
[<expression> for <item> in <sequence> if <condition>]  # If statement is optional
squared_c = [item ** 2 for item in mylist]

print(squared_for)
print(squared_c)

squared_small = [item ** 2 for item in mylist if item < 4]
print(squared_small)


# Miscellaneous 
[5, 'c', 2.5, {'a' : 1, 'b' : 2}]   # Is this a valid list?
a[:] is a                           # What will this return?

list_1 = [1, 2, 3, 4]               
list_2 = list_1                     # This is called aliasing, can be buggy
list_1[2] = 50                      
list_1                              # What will this return?
list_2                              # What will this return?

list_1 = [1, 2, 3, 4]
alist = list_1 * 3                   
blist = [list_1] * 3                 
>>> alist                           # What will this return?
>>> blist                           # What will this return?
list_1[0] = 5                       # 
>>> alist                           # What will this return?


# Nested / 2d lists
a = [[1, 2], [3, 4], [5, 6]]                        # How to access the 4?
x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']    # How would you access "z" in "baz"


# Shallow copy
alist = [1, 2, 3, [4, 5]]
blist = alist.copy()
blist[0] = 5
blist[3][0] = 10                    
blist                               # What will this return?
alist                               # What will this return? Why?
alist[3] is blist[3]                # What will this return?


# Deep copy
alist = [1, 2, 3, [4, 5]]
clist = copy.deepcopy(alist)  # To use this, you must import copy


# How can we create a 3 x 3 grid?
grid = []
for row in range(3):
    for col in range(3):
        grid.append(None)
print(grid)         # What will this print?


# How can we make it print like a 3 x 3 grid?
grid = []
for row in range(3):
    new_row = []
    for col in range(3):
        new_row.append(None)
    grid.append(new_row)
print(grid)         # What will this print?


# Printing 3 x 3 grid
for row in grid:
    print(row)


# What could be wrong with this?
grid = ([[None] * 3] * 3)
