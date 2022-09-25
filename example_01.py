my_str = input("Enter a string: ")

print("You entered : '" + my_str + "'")

myWordList = my_str.split()

print("My word list is : ")
print (myWordList)

myWordList.sort()
print("My sorted  word list is : ")
print (myWordList)

for myWord in myWordList:
	print(myWord)
