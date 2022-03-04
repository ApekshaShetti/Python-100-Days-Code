import random

# student_scores = [10, 20, 30, 40, 91]
# print(student_scores)
# high_score = 0
# for score in student_scores:
#     if score > high_score:
#         high_score = score
# print(high_score)


# sum = 0
# for i in range(1, 101, 2):
#     sum += i
# print(sum)


# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("Fizz Buzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# Easy level

l = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
s = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
n = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("Welcome to the PyPassword Generator")
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like?\n"))
numbers = int(input("How many numbers would you like?\n"))

# password = ""
# for char in range(1, letters + 1):
#     password += random.choice(l)
# for sym in range(1, symbols + 1):
#     password += random.choice(s)
# for num in range(1, numbers + 1):
#     password += random.choice(n)
# print(password)


# hard level

password_list = []
for char in range(1, letters + 1):
    password_list.append(random.choice(l))
for sym in range(1, symbols + 1):
    password_list.append(random.choice(s))
for num in range(1, numbers + 1):
    password_list.append(random.choice(n))
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is {password}.")
