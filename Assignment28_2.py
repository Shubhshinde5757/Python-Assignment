# Q2) Count Words in a File
file_name = input("Enter file name: ")

with open(file_name, "r") as file:
    text = file.read()

words = text.split()
print("Total number of words:", len(words))