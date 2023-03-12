months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']
print(months[0])  # January
print(months[1])  # February
print(months[7])  # August
print(months[-1])  # December
# print(months[25])  # IndexError: list index out of range

# Slicinh=g
list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[0])
# print(list_of_random_things[len(list_of_random_things)])
print(list_of_random_things[len(list_of_random_things) - 1])
print(len(list_of_random_things))
q3 = months[6:9]
print(q3)  # [ 'July', 'August', 'September']
first_half = months[:6]
print(first_half)  # ['January', 'February', 'March', 'April', 'May', 'June']
second_half = months[6:]
print(second_half)  # ['July', 'August', 'September', 'October', 'November', 'December']
print(len(months))  # 12
greeting = "Hello there"
print(len(greeting))  # 11
list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[1:2])
print(list_of_random_things[:2])
print(list_of_random_things[1:])


# In Operator
print('this' in 'this is a string')
print('in' in 'this is a string')
print('isa' in 'this is a string')
print(5 not in [1, 2, 3, 4, 6])
print(5 in [1, 2, 3, 4, 6])
my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'one'
print(my_lst)
greeting = "Hello there"
greeting[0] = 'M'
print(greeting)
