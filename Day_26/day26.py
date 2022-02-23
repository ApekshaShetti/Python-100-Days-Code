# List comprehension
# new list = [new_item for item in list]
# Conditional List comprehension
# new list = [new_item for item in list if test]


numbers = [1,2,3]
new_list = [n+1 for n in numbers]
print(new_list)

name = "Apeksha"
new_list = [letter for letter in name]
print(new_list)

range_num=range(1,5)
new_list = [n*2 for n in range_num]
print(new_list)

names = ["Apeksha","Neha","Zaid","Vinay","Anu","Netra","Om"]
new_list = [name for name in names if len(name)<5]
print(new_list)

names_in_uppercase = ["Apeksha","Neha","Zaid","Vinay","Anu","Netra","Om"]
new_list = [name.upper() for name in names_in_uppercase if len(name)>4]
print(new_list)

numbers=[1,1,2,3,5,8,13,21,34,55]
squared_num = [n*n for n in numbers]
print(squared_num)

num = [1,1,4,5,7,2,8]
even_num = [n for n in num if n%2==0]
print(even_num)

list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8,9]
equal_list = [int(num) for num in list1 if num in list2]
print(equal_list)
