class rectangle:
    def set_dim(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b

n= int(input("Enter the Number of Rectanle"))
shape=[]
for i in range(n):
    r=rectangle()
    l=int(input("Enter length of Rectangle {}".format(i+1)))
    b=int(input("Enter breadth of Rectangle {}".format(i+1)))
    r.set_dim(l,b)
    shape.append(r)
index=0
for i in shape:
    index=index+1
    res=i.area()
    print("Area of the Rectangle {} is {}")

