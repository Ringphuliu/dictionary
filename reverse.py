dic={"a":[3,2,1],"b":[7,6,5]}
b={}
for j in dic:
    x=dic[j]
    i=-1
    c=[]
    while i>=-len(x):
        c.append(x[i])
        i-=1
    b[j]=c
print(b)