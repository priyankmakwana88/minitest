#!/usr/bin/env python3

#IMPORTINNG LIBRARIES
from nltk.corpus import wordnet

#GETTING KEYWORD FROM USER
key=input("Enter any key word = ")

#PRINT THE LIST OF ALL THE BOOKS BASED ON KEYWORD
book=wordnet.synsets(key)

if len(book) ==0:
	print("no book availabe!!")

else:
	print("examples\t")
	print(book[0].examples())
	print("\n\ndefinition\t")
	print(book[0].definition())
