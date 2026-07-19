# Q5) Search a Word in a File

file_name = input("Enter file name: ")
word = input("Enter word to search: ")

with open(file_name, "r") as file:
    text = file.read()

if word in text:
    print(f"'{word}' is found in the file.")
else:
    print(f"'{word}' is not found in the file.")