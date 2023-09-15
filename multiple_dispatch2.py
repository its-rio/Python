from multipledispatch import dispatch


class calculate:
@dispatch(float, float)
def area(rad, pi):
ar = rad*rad*pi
print("Area of circle: ", ar)

@dispatch(float)
def area(len):
ar = len*len
print("Area of Square: ", ar)


pi = 3.14
ob1 = calculate()
ob1.area(5.2, pi)
ob1.area(5.5)
