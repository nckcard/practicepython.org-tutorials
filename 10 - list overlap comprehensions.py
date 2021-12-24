import random

a = random.sample(range(1,30),12)
b = random.sample(range(1,30),16)

results = [i for i in a if i in b]
results_unique = [i for i in results if results.count(i)==1]

print(a)
print(b)
print(results)
