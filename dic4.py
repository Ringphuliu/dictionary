# a={}
# for i in range(1,6):
#     a[i]=i*i b
#     # a[i]      
# print(a)

l={"a":10,"b":10}
s=0
for i in l:
    s=s+l[i]
print(s)

l=["one","two","three"]
i=0
a={}
while i<len(l):
    a[i+1]=l[i]
    i=i+1
print(a)