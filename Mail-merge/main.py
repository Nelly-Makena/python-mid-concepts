PLACEHOLDER = "[name]"


with open("names.txt") as names_file:
    names = names_file.readlines()


    print(names)

with open("startting-letter.txt") as letter:
    invites = letter.read()


    for name in names:

        stripped_name= name.strip()
        new_letter = invites.replace(PLACEHOLDER, stripped_name)
        print(new_letter)

        with open(f"ready_to_send/letter_for_{stripped_name}.txt", mode ="w") as completed_letter:
            completed_letter.write(new_letter)


