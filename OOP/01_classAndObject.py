class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def print(self):
        print(f"{self.a}+i{self.b}")
    def add(self, c):
        self.a += c.a
        self.b += c.b

c1 = Complex(10, 20)
print(c1.a, c1.b)
c1.print()
c2 = Complex(20, 30)
c1.add(c2)
c1.print()