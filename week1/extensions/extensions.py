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
        "txt":"text",
        "zip":"application",
        "plain":"application",
        "octet-stream":"application"
        }


for i in filetypes:
    if splited[-1]==i:
        type = filetypes[splited[-1]]
        break;
    if splited[-1]=="jpg":
        splited[-1]="jpeg"

    if  splited[-1]=="txt":
        splited[-1]="plain"

print(type+"/"+splited[-1])

