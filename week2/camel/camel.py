#!/usr/bin/env python3

"""
input --- > user inputs word in camel case
output ---> return word in snake case

camel case : first word is small letters, following words start with a capital letter

snake case : words are seperated by underscores("_")


proposed method:

for each character in camelCaseString:

    if character is uppercase:

        append the current container to listo

        container = "" # Start a new word

        convert the uppercase character to lowercase and add it to the new container

    else:

        add the character to the current container

After the loop, append the final container to listo

"""

def main():
    snake()

def snake():
    camel=input("camelCase: ")
    container=""
    listo=[]
  
    for i in camel:
        
        if i>="A" and i<="Z":
            listo.append(container)
            container=i.lower()
        else:
            container=container+i
            
    listo.append(container)
    
    snake=""
    

    list_len=len(listo)-1
    final_word=listo[list_len]

    for i in listo:
        if i=="":
            continue
        else:
            if final_word != i:
                snake+=i+"_"
            else:
                snake+=i
    
    return print(snake)
    
if __name__=="__main__":
    main()
