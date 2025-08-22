#!/usr/bin/env python3

"""

returns filetype and extension
Input ----> string from user
Output ----> filetype/file-extentions

"""

file_name=input("File name: ")

splited=file_name.lower().split(".")

filetypes={
        "gif":"image",
        "jpg":"image",
        "jpeg":"image",
        "png":"image",
        "pdf":"application",
        "txt":"document",
        "zip":"application",
        "plain":"application",
        "octet-stream":"application"
        }


for i in filetypes:
    if splited[-1]==i:
        type = filetypes[splited[-1]]
        break;
print(type+"/"+splited[-1])

