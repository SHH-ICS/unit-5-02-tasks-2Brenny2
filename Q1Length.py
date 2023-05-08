# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.

str = input("String: ")
while str.lower() != "quit":
    print(f"Length: {len(str)}")
    str = input("String: ")