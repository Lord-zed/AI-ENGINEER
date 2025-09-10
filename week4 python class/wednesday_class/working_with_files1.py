# This is how it works
# Using os.getcwd()

import os

# Get the current working directory
# print("current working directory:", os.getcwd())

# joining path
# import os
# folder = "C:/Users/Chris/Desktop"
# filename = "my_path.py"
# path = os.path.join(folder, filename)
# print("Full path:", path)


# checking if a file is on a folder
# import os
# path= "my_path.py"

# if os.path.exists(path):
#     print("yes, the file exists!")
# else:
#     print("file not found.")

# import os 
# path="working_with_files2"

# if os.path.exists(path):
#     print("yes, the file exists!")
# else:
#     print("file not found.")

# using pathlib
# from pathlib import Path

# # Get parent folder of current file
# print("Parent folder:", Path.cwd().parent)

# # List all files in a directory
# for file in Path.cwd().iterdir():
#     print(file)

# setting up

from pathlib import Path
workspace = Path("practice_files")
workspace.mkdir(exist_ok=True)
file_path = workspace / "notes.txt" 


# (A) Create or overwrite using 'w'
f = open(file_path, "w", encoding="utf-8")
f.write("This is the first line in notes.txt\n")
f.close()
 
# # # (B) Safe-create using 'x' (uncomment to try once)
# f = open(workspace / "created_once.py", "x", encoding="utf-8")
# f.write("This file will only be created if it doesn't exist.\n")
# f.close()

# # Open for writing again (this will overwrite!)
# f = open(file_path, "w", encoding="utf-8")
# f.write("Replaced the old content with this line.\n")
# f.close() 

# # write to a file
# f= open(file_path, "w" , encoding="utf-8")
# f.write("shopping list:\n")
# f.write(" _ Rice\n")
# f.write(" - Beans\n")
# f.write(" - Garri\n")
# f.close() 