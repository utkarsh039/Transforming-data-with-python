import read
import collections

hn_stories=read.load_data()
domains=hn_stories["url"]


domains2=domains.tolist()
nosubdomains=[]
for i in domains2:
    i=str(i)
    cnt=i.count(".")
    if cnt>=2:
        newstr=i.split(".",1)[1]
        nosubdomains.append(newstr)
    else:
        nosubdomains.append(i)
#print(collections.Counter(nosubdomains).most_common(100))
for name, row in domains.items():
    print("{0}: {1}".format(name, row))

