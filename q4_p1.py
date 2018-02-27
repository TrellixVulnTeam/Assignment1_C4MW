#file_path = input("Please enter file name: ")

d = {}
count = 0
# Open the file specified by the user and convert
f = open("test.txt", "r")
lines = f.readlines()
for line in lines:
    thisline = line.split(" ")
    for index in range(0, len(thisline)):
        if thisline[index] in d:
            d[thisline[index]] += 1
        else:
            d[thisline[index]] = 1
        index += 1

print(d)

str = "mystr\\n"
print(str)
str = str.rstrip("\n")
print (str)

