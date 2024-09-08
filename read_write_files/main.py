
#one method

# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

#method 2
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)


# method=3
# with open("my_file.txt", mode ="a" )as file:
#     file.write("\nIm dreaming of success ")
#
#     this one appends, w writes over, r readonly

# with open("new_file.txt", mode="w") as file:
#     file.write("This a file, I created...")
#
# this creates a new file if it wasnt there

