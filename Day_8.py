# def greet():
#     print("Hello")
#     print("Vanakkam")
#     print("Shubhprabhat")
# greet(new_paddle)

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"Vanakkam {name}")
#     print(f"Shubhprabhat {name}")
# greet_with_name("new_paddle")

# def greet_with_(name, location):
#     print(f"Hello {name}")
#     print(f"how is the weather in {location}")
# greet_with_("new_paddle", "India")

# def greet_with_(name, location):
#     print(f"Hello {name}")
#     print(f"how is the weather in {location}")
# greet_with_(location="India", name="new_paddle")

# import math
# def paint_calc(height, width, cover):
#     area = height * width
#     no_of_cans = math.ceil(area / cover)
#     print(f"Number of cans required is {no_of_cans} .")
# height_of_wall = int(input("Enter height of wall: \n"))
# width_of_wall = int(input("Enter width of wall: \n"))
# cover = 5
# paint_calc(height_of_wall, width_of_wall, cover)


# prime checker

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number - 1):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("it is a prime number")
#     else:
#         print("it is not a prime number")
# n = int(input("Check for this number: "))
# prime_checker(number=n)


# Ceasar Cipher

logo = """
   _____                           
  / ____|                          
 | |     __ _  ___  ___  __ _ _ __ 
 | |    / _` |/ _ \/ __|/ _` | '__|
 | |___| (_| |  __/\__ \ (_| | |   
  \_____\__,_|\___||___/\__,_|_|   
                                   
   _____ _       _               
  / ____(_)     | |              
 | |     _ _ __ | |__   ___ _ __ 
 | |    | | '_ \| '_ \ / _ \ '__|
 | |____| | |_) | | | |  __/ |   
  \_____|_| .__/|_| |_|\___|_|   
          | |                    
          |_|                    
"""
print(logo)


def caesar(plain_text, shift_amount, c_direction):
    text = ""
    for i in plain_text:
        if i in alphabets:
            position = alphabets.index(i)
            if c_direction == "encode":
                new_position = position + shift_amount
                new_letter = alphabets[new_position]
                text += new_letter
            elif c_direction == "decode":
                new_position = position - shift_amount
                new_letter = alphabets[new_position]
                text += new_letter
        else:
            text += i
    print(f"The {c_direction}d text is {text}")


alphabets = [
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
    "w",
    "x",
    "y",
    "z",
]

should_continue = True

while should_continue:
    direction = input('Type "encode" to encrypt, type "decode" to decrypt: \n')
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    shift = shift % 25

    caesar(text, shift, direction)
    result = input(
        "Type 'yes' if you want to go again. Otherwise 'no' to discontinue.\n"
    )
    if result == "no":
        should_continue = False
        print("GoodBye")
