list=["i","stay","in","navgurukul"]
i=0
c=[]
while i<len(list):
    j=0
    e=[]
    while j<len(list[i]):
        if list[i][j]==list[i][0]:
            b=list[i][0]
            c.append(b)
            d=",".join(c)
            e.append(d)
        j=j+1
    i=i+1
print(e)
