# www.jonathanblench.co.uk
# Script to generate a 3 word password and drop it into the clipboard to use
# Set path the word file as variable
wordfilepath = "britcaps.txt"
# Import the required modules
import random
import os
import sys
# Function to use clipboard
def addToClipBoard(text):
    command = 'echo ' + text.strip()
    os.system(command)
# Open and read the words file and split words
fileread1 = open(os.path.join(sys.path[0], wordfilepath), "r")
allcontent = (fileread1.read())
words = list(map(str, allcontent.split()))
# Generate 3 random words and store as variables
word1 = (random.choice(words))
word2 = (random.choice(words))
word3 = (random.choice(words))
#remove apostrophes from words
word1.replace("'","")
word2.replace("'","")
word3.replace("'","")
# Generate random 4 digit number
number = random.randint(1111,9999)
#convert number to string
convertednum = str(number)
# Bring words together into string and add dashes between words
password = word1+"-"+word2+"-"+word3+"-"+convertednum
# Remove hash from next line to print the password.
print (password)