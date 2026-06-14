#looping through a list 
numbers = [4, 7, 2, 6, 1]
for n in numbers: 
    print (n*2)

#convert celsius to fahrenheit 
def celsius_to_fahrenheit(c): 
    return (c * 9/5) + 32 

print(celsius_to_fahrenheit(0))
print(celsius_to_fahrenheit(32))
print(celsius_to_fahrenheit(100))

#dictionary with a for loop 
student = {
    "name": "Ayusha",
    "subject": "computer science", 
    "grade": 100, 
    "passed": True, 
    "age": 25, 
}

for key, value in student.items(): 
    print(f"{key}: {value}") # f string

#list comprehensions
third_power = [x**3 for x in range(1, 21)]
print(third_power)

odds = [x for x in range(20) if x % 2 != 0 ]
print(odds)

# While loop- count from 1 to 10 
i = 1
while i <= 10: 
    print (i)
    i += 1 

# Nested loop- multiplication table 
for i in range (1, 11): #the outer loop is like the hour hand 
    for j in range (1, 11): #the inner loop is like the minute hand
        print(f"{i} x {j} = {i * j}") 

# Function - sum and product 
def sum_and_product(a, b): 
    total = a + b 
    product = a * b 
    return total , product

result = sum_and_product(5, 5)
print(result)

