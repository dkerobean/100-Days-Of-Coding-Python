# # old way of working with files
# file = open("file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("file.txt") as file:
    contents = file.read()
    print(contents)

with open("file.txt", mode="a") as f:
    f.write("\n This is a new line")

with open("new_file.txt", mode="w") as nf:
    nf.write("writen to a new file")

# absolute file paths always start relative to the root
# relative file path is relative to your file directory(where you are currently working from)



