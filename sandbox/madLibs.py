print("Welcome to MadLibs!\n")
print("Answer the following questions and the program will generate a funny story!\n")
print("First, lets select a theme\n")

theme = (int) (raw_input("Select from the following themes \n1-Summer \n2-Something else \n3-Something else\n"))


def summerMadLibs():
    #YOUR INPUTS MUST BE RAW INPUTS!
#   word1 = raw_input("Insert an adjective -- 1/11\n")
    word1 = raw_input("Insert an adjective -- 1/11\n")
    word2 = raw_input("Type a noun; clothing -- 2/11\n")
    word3 = raw_input("Type a noun -- 3/11\n")
    word4 = raw_input("Type another noun -- 4/11\n")
    word5 = raw_input("Type yet ANOTHER noun -- 5/11\n")
    word6 = raw_input("Type a verb -- 6/11\n")
    word7 = raw_input("Type a noun; food -- 7/11\n")
    word8 = raw_input("Type another noun; food -- 8/11\n")
    word9 = raw_input("Type a noun; drink -- 9/11\n")
    word10 = raw_input("Type a verb -- 10/11\n")
    word11 = raw_input("Type a plural noun --11/11\n")

    print("\n---------------------------------------------------")
    print("Summer trips to the beach are so", word1+"!")
    print("Pack your", word2+", a", word3, "to dry yourself")
    print("off, and", word4, "to prevent sunburn. Be sure")
    print("to bring a", word5, "to", word6, "with")
    print("in the water, too. You can bring a beach")
    print("picinic, with", word7+",", word8+",", "and ", word9)
    print("to drink. Its fun to", word10, "for hours in the water")
    print("and to see", word11, "sail past in the distance!")
    print("---------------------------------------------------")

def otherMadLib():
    print("<insert a random hilarous story!>")

if (theme == 1):
    summerMadLibs()
    print ("\nHaha! What a great story!")

elif (theme == 2):
    otherMadLib()

elif (theme == 3):
    otherMadLib()

else:
    print("Thats not a valid input!")
