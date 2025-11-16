# 1. Perform Basic List Operations
# input: my_list = [10, 20, 30, 40, 50]
# output:
# Initial list: [10, 20, 30, 40, 50]
# Third item:  30
# Length of the list: 5
# list is not empty

my_list = [10, 20, 30, 40, 50]
print("Initial list:",my_list)
print("Third item:",my_list[2])
print("length of list:",len(my_list))
if my_list == 0:
    print("list is empty")
else:
    print("list is not empty")

#  2: Perform List Manipulation
# input:  my_list = [10, 20, 30, 40, 50]
# Output:
# Initial list: [10, 20, 30, 40, 50]
#
# After changing second element: [10, 200, 30, 40, 50]
# List after appending 600: [10, 200, 30, 40, 50, 600]
# List after inserting 300 at index 2: [10, 200, 300, 30, 40, 50, 600]
# List after removing 600 (by value): [10, 200, 300, 30, 40, 50]
# List after removing element at index 0: [200, 300, 30, 40, 50]

my_list = [10, 20, 30, 40, 50]
print("Initial list:",my_list)
my_list[1]=200
print("After changing second element:",my_list )
my_list.append(600)
print(" List after appending 600:",my_list)
my_list.insert(2,300)
print("List after inserting 300 at index 2:",my_list)
my_list.remove(600)
print(" List after removing 600 (by value):",my_list)
del my_list[0]
print("List after removing element at index 0:",my_list)

