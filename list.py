#wap to find the maximum number without using sort & max
l1 =[2,5,6,8,6,9,7,4,2]
m=l1[0]
for i in l1[1:]:
    if(m<i):
        m=i
print("greater: ",m)
