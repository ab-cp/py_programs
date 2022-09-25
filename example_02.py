listNames =[]

def menu_for_user():
	print("Please enter your choice")
	print("1 to add a name to the list")
	print("2 to sort the list")
	print("3 to remove a name from the list")
	print("4 to display the list of names")
	print("5 to exit program")
	print("Please enter your choice")
choice = 0
while(choice !=5):
	menu_for_user()
	choice = int(input("Please enter your choice: "))
	if (choice == 1):
		my_str = input("Enter a name: ")
		listNames.append(my_str)
		print (listNames)
	elif (choice == 2):
		print("Sorting the list of names in alphabetical order")
		listNames.sort()
		print("My sorted list is : ")
		print (listNames)
	elif (choice == 3):
		my_str = input("Enter a name to be removed: ")
		listNames.remove(my_str)
	elif (choice == 4):
		print("The list of names :")
		for name in listNames:
			print(listNames)   
	elif (choice == 5):
		print ("Exiting program...")
	
		
