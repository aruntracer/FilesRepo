class MathClass():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius

    def areaofsq(self):
        return self.radius * self.radius * MathClass.pi

mathobj = MathClass(2)
print(mathobj.radius)
print(mathobj.areaofsq())
