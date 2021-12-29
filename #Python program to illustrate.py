#Python program to illustrate
#while loop
count = 0
while (count < 5):
    count = count + 1
    print(str(count) + ": Hello Geek")
    
# for loop
n=4
print(range(0,n))
for i in range(0, n):
    print(i)

for i in range(3, 6):
    print(i)

for i in range(8, 20, 3):
    print(i)

# loop inside another loop
for i in range (1, 5):
    print ("Multiplication table for %d" % i)
    for j in range (0, 10):
        print ("%d * %d =%d"%(i, j, i*j))