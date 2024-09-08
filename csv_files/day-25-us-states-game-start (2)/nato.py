import pandas

data= pandas.read_csv("NATO.csv")

nato_dict = {row.Letter : row.Code for (index, row) in data.iterrows()}
def gen_word():
    choice=input("Enter a word?").upper()
    try:
        output = [nato_dict[Letter] for Letter in choice]

    except KeyError:
        print("Sorry, only letters in the alphabet please ")
        gen_word()
    else:
        print(output)

gen_word()

