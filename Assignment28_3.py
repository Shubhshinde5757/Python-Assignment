 # Q3) Display File Line by Line
 
file_name = input("Enter file name: ")

with open(file_name, "r") as file:
    for line in file:
        print(line, end="")