print("")
name = "Hi! I am Joshua Adrian O. Daet of BSCpE 1-4"
print(name.center(158))

sentence = "This is a program where you can decrypt a encrypted text"
print("")
print(sentence.rjust(106))
print("")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("")

# Ask the user to input the enrypted text
input_str = input("Enter the enrypted text: ")

output_str = ''  

for i in range(len(input_str)):
    if input_str[i] == "*":
        output_str += "a"
    elif input_str[i] == "&":
        output_str += "e"
    elif input_str[i] == "#":
        output_str += "i"
    elif input_str[i] == "+":
        output_str += "o"
    elif input_str[i] == "!":
        output_str += "u"
    else:
        output_str += input_str[i]
print("")

# Ouput of the decrypted text
print("The decrypted text is: " +output_str)
print("")