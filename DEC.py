'''class Mobile:
    def __init__(self, price, brand, ios_version):
        self.price=price
        self.brand=brand
        self.ios_version=ios_version
    def rt(self):
        return self.price

mob1=Mobile(2000, "Apple", 10)
mob2=Mobile(3000, "Samsung", "Marsh")
ob=Mobile(10)
print(ob.rt())'''

"""mob1.price=20000
mob1.brand="Apple"
mob1.ios_version=10

mob1.ios_version=11

mob2.price=3000
mob2.brand="Samsung"

mob2.android_version="Marshmallow" """

'''print(mob1.ios_version)
print(mob2.price)'''

f=open("narendra.txt", "w")
f.write("Hello everyone")
f.close()
x=open("narendra.txt", "r")
y=x.read()
print(y)
j=1
for i in y:
    if i==" ":
        continue
    j=j*1
    k=i*j
    print(k,end="")
