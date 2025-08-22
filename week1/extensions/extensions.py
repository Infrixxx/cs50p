#!/usr/bin/env python3

"""

returns filetype and extension
Input ----> string from user
Output ----> filetype/file-extentions

"""

file_name=input("File name: ")
no_space_low=file_name.strip().lower()  #strip all white spaces
splited=no_space_low.split(".")         #split into array
extension=splited[-1]                   #take ext from array


filetypes = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

if extension in filetypes:
    print (filetypes[extension])

else:
    print ("application/octet-stream")
