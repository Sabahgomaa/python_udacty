countries = ['Angola', 'Maldives', 'India', 'United States', 'India', 'Denmark', 'Sweden', 'Ghana', ]

print(len(countries))  # 785
print(countries[:5])  # ['Angola', 'Maldives', 'India', 'United States', 'India']

country_set = set(countries)
print(country_set)  # 196

country_set.add('Italy')

numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)
fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
print(b)
b.pop()
print(b)