from collections import defaultdict
from random import choice

def addWord(currWord, wordMap, iter, maxIter = 10):
	if iter >= maxIter:
		return ""
	try:
		nextWord = choice(wordMap[currWord])
	except:
		return ""
	return nextWord + " " + addWord(nextWord, wordMap, iter + 1, maxIter)


wordMap = {}
inputText = None
fileLoc = "markovInput.txt"

try:
	inputText = open(fileLoc, "r").read()
except:
	print("File not found or invalid")
	quit()

prevWord = None
for word in inputText.split():
	if prevWord == None:
		prevWord = word
		continue
	try:
		wordMap[prevWord].append(word)
	except:
		wordMap[prevWord] = [word]
	prevWord = word
			
	
print addWord(choice(inputText.split()), wordMap, 0, 1000)
