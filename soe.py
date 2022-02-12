#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3

# Python program to find sum of elements in list
total = 0

# creating a list
# list1 = [11, 5, 17, 18, 23]
list1 = eval(input('Enter a list: '))
print (' The list is ', list1)

# Iterate each element in list
# and add them in variable total
for ele in range(0, len(list1)):
	total = total + list1[ele]

# printing total value
print("Sum of all elements in given list: ", total)
