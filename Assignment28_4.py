#Q4) Copy File Contents into Another File


source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

with open(source, "r") as file1:
    data = file1.read()

with open(destination, "w") as file2:
    file2.write(data)

print("Contents copied successfully.")