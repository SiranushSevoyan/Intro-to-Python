import sys

print(sys.argv[1:])

list1= ['hello', 1, True]
list2=sys.argv[1:]
list1.append(list2)
print(list1)
list1= ['hello', 1, True]
list1.extend(list2)
print(list1)