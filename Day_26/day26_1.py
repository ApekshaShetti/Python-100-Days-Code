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

import random

# Dictionary Comprehension
# new_dict={new_key:new_value for item in list}
# new_dict={key:value for (key,value) in dict.items() if test}

dic_names=["Apeksha","Neha","Zaid","Vinay","Anu","Netra","Om"]
students_score={student:random.randint(1,100) for student in dic_names}
print(students_score)

passed_students={student:score for (student,score) in students_score.items() if score > 50}
print(f"Students who are passed are: {passed_students}")

sentence="What is the Airspeed Velocity of an Unladen Swallow?"
list_1=sentence.split()
dict={word:len(word) for word in list_1}
print(dict)

weather_c={
    "Monday":12,
    "Tuesday":14,
    "Wednesday":15,
    "Thursday":14,
    "Friday":21,
    "Saturday":22,
    "Sunday":24
}

weather_f={day:temp_c*9/5+32 for (day,temp_c) in weather_c.items()}
print(weather_f)


# pandas
                # import pandas

                # student_dict={
                #     "student":["Apeksha","Neha"],
                #     "score":[55,54]
                # }

                # student_data_frame=pandas.DataFrame(student_dict)
                # print(student_data_frame)

# Loop through a dataframe

# for (key,value) in DATAFRAME.items():
#     print(key/value)

# Loop through rows of a dataframe

# for (index,row) in DATAFRAME.iterrows():
#     if row.student=="":
#         print(row.score)
