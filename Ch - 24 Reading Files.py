empolyee_file = open("Ch - 24 empolyees.txt", "r")
print(empolyee_file.readable())
empolyee_file.close()

empolyee_file = open("Ch - 24 empolyees.txt", "r")
print(empolyee_file.readline())
empolyee_file.close()

empolyee_file = open("Ch - 24 empolyees.txt", "r")
print(empolyee_file.read())
empolyee_file.close()

empolyee_file = open("Ch - 24 empolyees.txt", "r")
print(empolyee_file.readlines())
empolyee_file.close()

empolyee_file = open("Ch - 24 empolyees.txt", "r")
print(empolyee_file.readline())
print(empolyee_file.readline())
empolyee_file.close()

empolyee_file = open("Ch - 24 empolyees.txt", "r")
print(empolyee_file.readlines()[2])
empolyee_file.close()

empolyee_file = open("Ch - 24 empolyees.txt", "w")
print(empolyee_file.readable())
empolyee_file.close()
# Note: Using 'w' mode will overwrite the file and delete any existing content in "Ch - 24 employees.txt"