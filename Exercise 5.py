import random

a = [5, 10]
b = [1, 5]
for i in range(10):
    a.append(random.randint(1, 42))
    b.append(random.randint(1, 138))

c = []
print a
print b
for i in b:
    if i in a:
        c.append(i)

print c
