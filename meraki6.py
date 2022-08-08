dic={"ball":"red","bat":4,"wicket":8,"ball":"given","bat":3}
dic1={}
for i in dic:
    if dic[i]not in dic1:
        dic1[i]=dic[i]
print(dic1)