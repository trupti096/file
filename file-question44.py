a=open("file-question4.txt","r")
b=a.read()
c=open("delhi.txt","w")
d=open("shimla.txt","w")
e=open("others.txt","w")
f=b.split("\n")
i=0
while i<len(f):
    if "delhi" in f[i]:
        c.write(f[i])
        c.write("\n")
    elif "shimla" in f[i]:
        d.write(f[i])
        d.write("\n")
    else:
        e.write(f[i])
        e.write("\n")
    i=i+1
a.close()