import re
sentence ="I love Avengers Avengers"
print (re.sub(r"Avengers","Justice League",sentence))
print (re.sub(r"[a-z]","0",sentence,5,flags=re.I))
#short hand classifieer
sentence1="welcome to year 2019"
sentence2= "Just ~%    +++++-------arriverd at @Jack's place. #fun"
sentence3 ="I                love          you"
sentence1_modified = re.sub(r"\d"," ",sentence1)
sentence2_modified = re.sub(r"[@#~+-\.']","",sentence2)
sentence2_modified = re.sub(r"\W"," ",sentence2)#remove all the ascii symbols
sentence2_modified = re.sub(r"\s+"," ",sentence2_modified)#replacing one or more spaces with a single space
sentence2_modified = re.sub(r"\s+[a-zA-Z]\s+"," ",sentence2_modified)
sentence3_modified = re.sub(r"\s+"," ",sentence3)
print (sentence2_modified)
print (sentence3_modified)
print (sentence1_modified)