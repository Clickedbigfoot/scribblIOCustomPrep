#!/usr/bin/python

"""
Prevents duplicates and bad formatting in skribbl io custom words paragraphs
"""

INPUT_FILE = "skribblIO.txt" #File to read the custom words from
OUTPUT_FILE = "skribblIO_unique.txt" #File to print the custom words list without duplicates

inputData = open(INPUT_FILE, "r")
words = [] #List of words
cur = "" #Current word being parsed
vocab = set([]) #Keep track of duplicate words
for line in inputData.readlines():
	#Iterate through every line in the text file
	cur = "" #reset
	for char in line:
		#Iterate through every character in the line
		if char != ",":
			#It is part of a word
			if char == "'":
				#It is an apostrophe, which needs to be filtered out
				continue
			else:
				cur = cur + char.lower()
		else:
			#It is a comma
			cur = cur.strip()
			if len(cur) == 0:
				#There is no valid string to add
				continue
			if cur in vocab:
				#Word already there
				cur = ""
				continue
			else:
				#Word not encountered yet
				vocab.add(cur)
				words.append(cur)
				cur = ""
	cur = cur.strip() #Get rid of whitespace
	if cur in vocab:
		#Word already there
		cur = ""
		continue
	else:
		#Word not encountered yet
		if len(cur) == 0:
			#Word is an empty string
			continue
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
