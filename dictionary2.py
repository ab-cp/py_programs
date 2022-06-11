Dict = {}
print("Empty Dictionary: ")
print(Dict)

Dict[0] = 'Zero' 
Dict[2] = 'Eight'
Dict[3] = 'Three'
print("\nDictionary after adding 3 elements: ")
print(Dict)

Dict[2] = 'Two'
print("\nUpdated key value: 2")
print(Dict)

my_key = int(input("Enter Key: "))
my_value = input("Enter Value: ")
Dict[my_key] = my_value

print("\nDictionary after adding %d", my_key)
print(Dict)


