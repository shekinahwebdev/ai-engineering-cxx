import os

# relative path
file_path = os.path.join(os.path.dirname(__file__), "notes.txt")

with open(file_path, 'r') as write_file:

   print(write_file.read())


# absolute path
try: 
   with open("/Users/patriciakanneh/ai-engineering/python/exercises/file-handling/note.txt") as read_file:
    print(read_file.read())

except FileNotFoundError:
   print("File not found.")


# opening a file to read it, if it doesn't exist, return an error(default)
with open(file_path , 'r') as file:
   print(file.read())

# opening a file to write it, if it doesn't exist, return an error
with open(file_path, "w") as file:
   file.write("Hi again")

with open(file_path, "r") as file:
   print(file.read())

# opening a file to append texts into it, if it doesn't exist, creates it
with open(file_path, "a") as file:
   file.write("Adding another line of texts")

with open(file_path, "r") as file:
   print(file.read())


file_path = os.path.join(os.path.dirname(__file__), "open.txt")

# creating a file, if it doesn't exist, create one
try:
   with open(file_path, "x") as file:
    file.write("Hello Tech World!")

   with open(file_path, "r") as file:
    print(file.read())

except FileExistsError:
   print("File already exists")


fb = open(file_path, "r")
print(fb.read())

fb.close()


file_name = input("Enter file name: ")

file_p = os.path.join(os.path.dirname(__file__), file_name)

with open(file_p, "x") as file:

   file_content = input("Enter a content for the file: ")
   file.write(file_content)

with open(file_p, "r") as file:
   print(file.read())


for i in range(1,4):
   file_p = os.path.join(os.path.dirname(__file__), f"day{i}.txt")
   
   with open(file_p, "x") as file:
      file.write(f"Hello {i}")

with open(file_p, "r") as file:
   print(file.read())
   print(file.read())
   print(file.read())


