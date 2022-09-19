import re
import pickle

file1 = open('nya', 'r', encoding="utf8")
Lines = file1.readlines()
count = 0	


try:
	with open('nya.pickle', 'rb') as handle:
	    wordCount = pickle.load(handle)
except:
	wordCount = dict()


for line in Lines:
	result = re.sub(r'[^A-Za-z ]', '', line)
	x = result.split()
	for i in x:
		if i.upper() not in wordCount:
			wordCount[i.upper()] = 1
		else:
			wordCount[i.upper()] = wordCount[i.upper()] + 1


wordCount = dict(sorted(wordCount.items(), key=lambda item: item[1]))			

for i in wordCount:
	print(i,wordCount[i])
	
with open('nya.pickle', 'wb') as handle:
    pickle.dump(wordCount, handle, protocol=pickle.HIGHEST_PROTOCOL)



