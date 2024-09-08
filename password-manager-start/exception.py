
#this are used to handle  exception errors that we dont counter to avoid the program crashing

try:#Where u put in ur problematic code
    file = open("a_file.txt")
    a_dictionary ={"key" : "value"}
    print(a_dictionary["dsfsdjjd"])


except FileNotFoundError: #or except IndexError,  #helps the program not to crush, incase the try is produces an error

    file =open ("a_file.txt", "w")
    file.write("Something ")


except KeyError as error_message:
    print(f"THe key {error_message}doesnt exist")

else:#excutes when there was no exception error
    content= file.read()
    print(content)
finally: #runs when no matter what happens
    file.close()
    print("Finally i closed the file ")

    raise TypeError("This is an error i made up ")# used to create ur own errors
    #Eg
    #we were to calculate the BMI of humans, taking the weight and the height
    # if height > 3:
    #     raise ValueError("Human height cant be greater than 3 ")
    # bmi = weight /height *=2
    # print(bmi)
