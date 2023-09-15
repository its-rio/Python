from multipledispatch import dispatch
@dispatch(int)
def area(r):
    ar = 3.17 * r* r
    print("Area of circle=",ar)
@dispatch(int, int)
def area(l, b):
    ar = l * b
    print("Area of rectangle=",ar)
area(5) 
area(3,7)


