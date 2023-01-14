print("program started!")
print("pplease enter a standered character:")

character = input()

if (len(character) == 1):
   print("The ASCII code for {} is {}".format(character, ord(character))
else:
    print("A single character was expected.")

print("Program Ended!")