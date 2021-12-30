p=open("people1-exercise2.txt","r")
print(p.readline())
i=0
count=0
while i<len(p):
    count=count+1
    i=i+1
    print(count)