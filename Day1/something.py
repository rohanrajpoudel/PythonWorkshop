# my_tuple = (1, 2, 3, 'hello')
# # Accessing elements in a tuple
# print(my_tuple[0])  # Output: 1
# print(my_tuple[-1])  # Output: 'hello'
# # Slicing a tuple
# print(my_tuple[1:3])  # Output: (2, 3)
# print(my_tuple[::2])  #[start:end:step]
# # Checking membership
# print(2 in my_tuple)  # Output: True
# print('world' in my_tuple)  # Output: False

# my_list = [1, 2, 3, 'hello']
# # Adding elements to the end of the list
# my_list.append(4)
# print(my_list)  # Output: [1, 2, 3, 'hello', 4]
# my_list.extend([5, 6])
# print(my_list)  # Output: [1, 2, 3, 'hello', 4, 5, 6]
# # Inserting/removing elements at a particular position
# my_list.insert(2, 'world')
# print(my_list)  # Output: [1, 2, 'world', 3, 'hello', 4, 5, 6]
# my_list.remove('world')
# print(my_list)  # Output: [1, 2, 3, 'hello', 4, 5, 6]
# # Pop and Delete
# popped_element = my_list.pop(2)
# print(popped_element)  # Output: 3
# del my_list[0]
# print(my_list)  # Output: [2, 'hello', 4, 5, 6]

# # Disctionary
# my_dict = {'Name': 'My Name', 
#            'Some Key': [2, 4, 3]}
# next_dict = {'name': 'John', 
#            'age': 30, 
#            'city': 'New York'}
# print(next_dict['age'])  # Output: 30

# # Sets
# my_set = {1, 2, 3, 4, 5, 5, 5} 
# print(my_set) # Output: {1, 2, 3, 4, 5}
# next_set = {1, 2, 3, 4, 5}
# next_set.add(6)
# print(next_set)  # Output: {1, 2, 3, 4, 5, 6}

# # If statement
# x = input("Enter a number: ")
# x = int(x)
# if x < 0:
#     print('Negative')

# # If else statement
# x = input("Enter 0 or 1: ")
# if x == '0':
#     print('False')
# else:
#     print('True')

# If elif else statement
x = input("Enter your percentage: ")
x = int(x)
if x >= 90:
    print('A')
elif x >= 80:
    print('B')
elif x >= 70:
    print('C')
elif x >= 60:
    print('D')
else:
    print('Fail')


# # For loop
# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(fruit)
# for i in range(5):
#     print('i'*i)

# # While loop
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# z = input("Yes/no?")
# while z != 'no':
#     z = input("Yes/no?")

# # continue and break
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(10):
#     print(i)    
#     if i == 5:
#         break
