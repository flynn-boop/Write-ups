#!/usr/bin/python3

#Caeser cipher brute forcer
#takes a filename with the characters as input
#outputs to the screen
import sys

def shift_letter(letter, shift): # takes in the letter and shift and outputs the shifted letter
    num=ord(letter)
    num= num+shift
    if (num>122): # loops around alphabet
        num-=26
    out=chr(num)
    return(out)

def main():
    fh=open(sys.argv[1], "r")
    ciphert=fh.read()
    fh.close()
    ciphert=ciphert.lower() #makes sure lowercase
    x=0
    i=0
    lciphert=list(ciphert)
    print("")
    for x in range(1,26): #cycles through all keys
        plaint=""
        lciphert=list(ciphert)
        for i in range(0, len(lciphert)):

            if lciphert[i].isalpha(): #decrypts letter
                lciphert[i]=shift_letter(lciphert[i], x)
            plaint+=lciphert[i]
        print(plaint)

main()
