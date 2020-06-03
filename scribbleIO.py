#!/usr/bin/python

"""
Prevents duplicates and bad formatting in scribble io custom words paragraphs
"""

INPUT_FILE = "scribbleIO.txt" #File to read the custom words from
OUTPUT_FILE = "scribbleIO_unique.txt" #File to print the custom words list without duplicates

inputData = open(INPUT_FILE, "r")
words = [] #List of words
cur = "" #Current word being parsed
vocab = set([])
for line in inputData.readlines():
	#Iterate through every line in the text file
	cur = "" #reset
	for char in line:
		#Iterate through every character in the line
		if char != ",":
			#It is part of a word
			if char == "'":
				cur = cur + char
			else:
				cur = cur + char.lower()
		else:
			#It is a comma
			cur = cur.strip() #Get rid of whitespace
			if cur in vocab:
				#Word already there
				cur = ""
				continue
			else:
				#Word not encountered yet
				vocab.add(cur.strip())
				words.append(cur)
				cur = ""
	if cur in vocab:
		#Word already there
		cur = ""
		continue
	else:
		#Word not encountered yet
		vocab.add(cur)
		words.append(cur)
		cur = ""
inputData.close()
output = open("OUTPUT_FILE", "w+")
for word in words[:len(words) - 1]:
	#Iterate through every word in scribble io list
	output.write(word + ",")
output.write(words[len(words) - 1])
output.close()