Data = []

MAX_BUFFER = 20
sum = 0
old = 0
youngest = 0

for x in range(1,MAX_BUFFER+1):
	y = input("Enter Number %d :" %x)
	y=int(y)
	Data.append(y)
	print (Data)
	
youngest = Data[0]
old = Data[0]


for x in range(10):
	print("Before Step %d: a(%d) sum(%d) old(%d) youngest(%d)" % (x,Data[x],sum, old, youngest))
	sum=sum+Data[x]
	if old < Data[x]:
		old = Data[x]
	if youngest > Data[x]:
		youngest = Data[x]
	print("After step[%d]: a(%d) sum(%d) old(%d) youngest(%d)" % (x,Data[x],sum, old, youngest))

print("The sum of all the elements in the list is %d" % sum)
print("The maximum number from the list is %d" % old)
print("The minimum number from the list is %d" % youngest)
