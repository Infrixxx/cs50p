#!/usr/bin/env python3

"""

returns filetype and extension
Input ----> string from user
Output ----> filetype/file-extentions

"""

file_name=input("File name: ")

splited=file_name.split(".")

filetypes={
        "gif":"image",
        "jpg":"image",
        "jpeg":"image",
        "png":"image",
        "pdf":"document",
        "txt":"document",
        "zip":"archive"
        }


print(filetypes)
