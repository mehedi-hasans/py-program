name = input("What's your name? ").strip().title()

#Remove white space from str
# name = name.strip()

#Capitalize users name
# name = name.title()

# name = name.strip().title()
# print('Hello, ' + name)

#split user's name into first name and last name
first, last = name.split(' ')
print(f'Hello, {first}')



# a = int(input('Enter A Value: '))
# b = int(input('Enter B Value: '))
# c = int(input('Enter C Value: '))

# if a > b and b > c:
#     print("A")
# elif b >a and b > c:
#     print("B")
# else:
#     print('C')