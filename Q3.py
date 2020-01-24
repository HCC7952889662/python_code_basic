s = input("Please input a list of string\n")
sentence = s.split(" ")

word = input("Please input a string\n")

if word not in sentence:
    print("String was not found")
else:
    print(word);
