import time

# get the start time
st = time.time()

numbers = range(100000)
for x in numbers:
    if (x % 2) == 0:
        print(x)

# get the end time
et = time.time()
# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')