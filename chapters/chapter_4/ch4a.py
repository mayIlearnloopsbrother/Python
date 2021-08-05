#!/usr/bin/python3 

#THIS PROGRAM MAKE USES OF FOR LOOP LIST RANGE WITH 2 OR MORE VALUES  


for a in range(1,20):
	print(a)

n = list(range(1,1000000))

print("\nmin: " + str(min(n)) + "\nmax: " +str(max(n)) + "\nsum: " + str(sum(n)))

odd = list(range(1,20,2))
print("\n")
print(odd)

mul = []
for a in range(1,11):
	mu = a*3
	mul.append(mu)
print("\n")
print(mul)

cube =[]
for cu in range(1,11):
	c = cu**3
	cube.append(c)
print("\n")
print(cube)

cubes = [a**3 for a in range(1,11)]
print("\n")
print(cubes)
