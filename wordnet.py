import nltk
from nltk.corpus import wordnet
handel=open("/home/venish/Pictures/wordnet.txt")
li=handel.readlines()
list_word=[]
for i in li:
    inde=i.find("\n")
    list_word.append(i[:inde])
#nltk.download()
ar=[]
for i in list_word:
    a=wordnet.synsets(i)
    for j in a:
        ar.append(j.lemmas()[0].name())
ls=[]
for i in ar:
    if i in ls:
        continue
    else:
        ls.append(i)
handel=open("wrordnet_final_list","a")
for i in ls:
    print(i,file=handel)
handel.close()
