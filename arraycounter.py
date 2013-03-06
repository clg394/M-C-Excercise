from collections import Counter
print ("Enter the values for your array below. When finished typed 'done'. The program will list the number of occurances")
ar=input("Enter a value for your Array: ")
a=[]
while ar != 'done':
        a.append(ar)
        ar=input("Enter a value for your Array: ")
        
bb=(Counter(a).most_common())
b=bb.sort()
c=0
while True:
    if c<len(bb):
        d=bb[c][0]
        e=bb[c][1]
        print ("The value", d, "occurs", e, "times.")
        c+=1
    else: break
