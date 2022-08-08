sinfo={"id":1234,"name":"raju","rollno":21}
for a in sinfo:
    print(a,":",sinfo[a])

# def no_space(x):
#     y=x.split()
#     z="".join(y)
#     return z
# x="P y thon"
# print(no_space(x))
# l="the and"

# def between(a,b):
#     l=[]
#     i=a
#     while i<=b:
#         l.append(i)
#         i+=1
#     return l

# print(between(1,4))
# def func(text):     
#     # text="ring kahmei"
#     a=text.split()
#     print(a)
# func("ring kahmei")


    


  
def is_palindrome(s):
    a=s.upper()
    s1=""
    i=-1
    while i>=-len(a):
        s1+=a[i]
        i-=1
    # if a==s:
    #     return True
    # else:
    #     return False
    print(s1)
    print(a)
# is_palindrome("a")
is_palindrome("Abba")
