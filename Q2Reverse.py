# Create a program that will accept a word and output the word one letter at a time in reverse.

str = input("String: ")
for i in range(len(str)): print(str[::-1][i])