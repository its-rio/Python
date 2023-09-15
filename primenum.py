#wap to prime number

l1=[3,7,5,9,2,6,5]
c=0
for i in l1:
    f=0
    for j in range(2,i):
        if(i%j==0):
            f=1
            break
    if(f==0):
        c+=1
        print("prime number",i)
    print("Total",0)    
