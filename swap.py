
a=2
b=3
print("before swapping",a,b)
#logic 1
a=a+b
b=a-b
a=a-b

#logic 2
a,b=b,a
print("After swapping",a,b)
