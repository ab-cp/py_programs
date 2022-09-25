listNums =[]

def menu_for_user():
	print("Please enter your choice")
	print("1 to add a number to the list")
	print("2 to sort the list")
	print("3 to remove a number from the list")
	print("4 to display the list of numbers")
	print("5 to exit program")
choice = 0
while(choice !=5):
	menu_for_user()
	choice = int(input("Please enter your choice: "))
	if (choice == 1):
		my_str = int(input("Enter a number: "))
		listNums.append(my_str)
		print (listNums)
	elif (choice == 2):
		print("Sorting the list of numbers least to greatest")
		listNums.sort()
		print("My sorted list is : ")
		print (listNums)
	elif (choice == 3):
		my_str = int(input("Enter a number to be removed: "))
		listNums.remove(my_str)
	elif (choice == 4):
		print("The list of numbers :")
		for idx, number in enumerate(listNums):
			print(idx, number)   
	elif (choice == 5):
		print ("Exiting program...")
	
		
