import random
MyRandomList = []
MyPrimeResult=[]
is_prime_number = True
for i in range(0, 20):
	n = random.randint(1,1000)
	MyRandomList.append(n)
print (MyRandomList)
for x in MyRandomList:
	is_prime_number = True
	print("Checking if %d is prime" % x)
	if x > 1:
		for i in range (2,x):
			if x % i==0:
				print ("%d is divisible by %d ,hence it is not prime" % (x, i))
				is_prime_number =False
				break
		if is_prime_number == True:
			print("%d is not divisible by any number greater than 1 and itself,hence it is prime" % (x))
			MyPrimeResult.append(n)
print (MyPrimeResult)
