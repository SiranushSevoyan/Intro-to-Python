import sys

print(sys.argv[1:])

list1= ['hello', 1, True]
list2= sys.argv[1:]
list3=list1.copy()

list3.extend(list2)
print(list3)