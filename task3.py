string = input("Enter your string: ")
letter = string[0]
if letter in ['a', 'e', 'i', 'o', 'u']:
    string = string + "hay"
    print(string)
else:
    string = string[1:] + letter + "ay"
    print(string)