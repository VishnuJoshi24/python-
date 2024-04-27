numbers = [10, 20, 30, 40, 50]

# list comprehension to create new list
doubled_numbers = [num * 2 for num in numbers]

print(doubled_numbers)

# Reads two numbers from input and typecasts them to int using 
# list comprehension
x, y = [int(x) for x in input().split()]
print(x)
print(y)

# Reads two numbers from input and typecasts them to int using 
# map function
x, y = map(int, input().split())
print(x)
print(y)