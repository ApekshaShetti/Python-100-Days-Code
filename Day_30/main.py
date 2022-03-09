# FileNotFound

try:
    file = open("a_file.txt")
    dict = {"Key":"Value"}
    print(dict["abc"])
except FileNotFoundError:
    # print("There was an error ")
    file = open("a_file.txt","w")
    file.write("Write something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")

    