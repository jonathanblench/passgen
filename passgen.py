# www.jonathanblench.co.uk
# Script to generate a 3 word password and drop it into the clipboard to use
# Set path the word file as variable
wordfilepath = "britcaps.txt"
# Import the random module
import random
# Function to use clipboard
import os
def addToClipBoard(text):
    command = 'echo ' + text.strip()
    os.system(command)
# Open and read the words file and split words
fileread1 = open(wordfilepath, "r")
allcontent = (fileread1.read())
words = list(map(str, allcontent.split()))
# Generate 3 random words and store as variables
word1 = (random.choice(words))
word2 = (random.choice(words))
word3 = (random.choice(words))
# Bring words together into string and add dashes between words
password = word1+"-"+word2+"-"+word3
# Place password into clipboard and display
addToClipBoard(password)
# Remove hash from next line to print the password.
print (password)