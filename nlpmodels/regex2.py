import re
X = ["This is a wolf #scary","Welcome to the jungle #missing","11322 the number to know","remember the name s - John","I love                    you"]
for i in range(0,len(X)):
	X[i] = re.sub(r"\W"," ",X[i])#removing the ascii characters
	X[i] = re.sub(r"\d"," ",X[i]) #removing the digits
	X[i] = re.sub(r"\s+[a-z]\s+"," ",X[i],flags= re.I)#removing the spaces before and after the words
	X[i] = re.sub(r"^\s","",X[i])# removing the spaces in front of the sentences
	X[i] = re.sub(r"\s$","",X[i])#removing spaces at the end of the sentences
	X[i] = re.sub(r"\s+"," ",X[i])# removing all the extra spaces in between the sentences
for i in range(len(X)):
	print (X[i])