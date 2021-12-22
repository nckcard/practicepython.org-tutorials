number = int(input("Choose an integer greater than 2: "))

x = range(2,number)
b = []

for element in x:
  if number % element == 0:
    b.append(element)

print("Divisors of " + str(number) + ":")
print(b)
