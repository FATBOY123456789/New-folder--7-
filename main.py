class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,b):
        if self.a<b.a:
            return 'ob1 is less than ob2'
        else:
            return 'ob1 is greater than ob2'
    def __eq__(self,b):
        if self.a==b.a:
            return 'ob1 is equal to ob2'
        else:
            return 'ob1 is not equal to ob2'

ob1=A(2)
ob2=A(2)

print(ob1<ob2)
print(ob1==ob2)

ob3=A(2)
ob4=A(3)
print(ob3<ob4)
print(ob3==ob4)

ob5=A(3)
ob6=A(2)
print(ob6<ob5)
print(ob5==ob6)