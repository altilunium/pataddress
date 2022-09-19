import pickle
with open('nya.pickle', 'rb') as handle:
	wordCount = pickle.load(handle)

wordCount = dict(sorted(wordCount.items(), key=lambda item: item[1],reverse=True))			

c = 0
l = []
for i in wordCount:
	if (len(i) < 9):
		#print(i)
		c = c + 1
		l.append(i)
	#print(i,wordCount[i])

print(l)
print(c)