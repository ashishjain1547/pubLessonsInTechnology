import math
n = int(input("The number:"))

sqrt_n = math.ceil(math.sqrt(n))

l = set({})

for i in range(1, sqrt_n + 1):
    if n % i == 0:
        q, r = divmod(n, i)
        l.add(i)
        l.add(q)

print(l)
print(len(l))