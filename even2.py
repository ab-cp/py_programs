import time


st = time.time()

numbers = range(1000000001)
for y in numbers:
	#print (y%2)
	remainder=y%2
	if remainder==0:
		print (y)

et = time.time()
elapsed_time = et - st
print ('Execution time:', elapsed_time, 'seconds')