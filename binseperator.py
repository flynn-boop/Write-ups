#!/usr/bin/python3
import sys

#program divides a message into seperate bins. the number of bins is first arguement
#second arguement is the filename with the message
def main():
  nbins=int(sys.argv[1])
  fh=open(sys.argv[2], "r")
  message=fh.read()


#each bin is like a mod nbins
  for x in range(0,nbins):
    bin=""
    k=x
    while k<len(message):
      bin+=message[k]
      k+=nbins
    print("Bin", str(x)+":",bin)

main()
