s=input()
c=0
d=0
e=0
for i in s:
    if ord(i)==97 or ord(i)==101 or ord(i)== 105 or ord(i)==111 or ord(i)==117 or ord(i)==65 or ord(i)==69 or ord(i)==73 or ord(i)==79 or ord(i)==85:
        c=c+1
    elif ord(i)==32:
        d=d+1
    else:
        e=e+1
print("vowels={} const={} space={}".format(c,e,d))        
