import random
a= []
for i in range(10):
	a.append(random.randrange(1,100))

print a
print sorted(a)
for i in a:
	for j in range(len(a)-1):
		if a[j] > a[j+1]:
			a[j], a[j+1]= a[j+1], a[j]

print a
