# write a code to generate a list of n fabonici terms with reverse order
lst=[]
a=0
b=1
ans=0
n=int(input("Enter the number::"))
for i in range(n):
    ans=ans+a
    lst.append(ans)
    a=b
    b=ans
   
rev=lst[::-1] 
print(rev)
