import urllib
import re

y=raw_input("Enter Search:")
z=y.replace("#","%23")
s=z.split();
i=1
terms=[]
terms.append(s[0])
while i< len(s):
    terms.append("+")
    terms.append(s[i])
    i+=1
d= ' '.join(terms)
fin=d.replace(" ","")
url=["https://twitter.com/search?q="+fin+"&src=typd"]
i=0
w=1
regex='<span class="js-display-url">(.+?)</span>'
pattern=re.compile(regex)
final=[]
ww=0
print ("")
print ("The Top Links Are:")
while True:
    while i<w:
        htmlfile=urllib.urlopen(url[i])
        htmltext=htmlfile.read()
        titles=re.findall (pattern, htmltext)
        yy=titles
        final.extend(yy)
        break
    while ww<len(yy):
        print final[ww]
        ww+=1

        
        


    





