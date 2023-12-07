#base class
class person:
    def display(self):
        print("This is class person")

#derived class 1
class employee(person):
    def printing(self):
        print("This is derived class employee")

class programmer(employee):
    def show(self):
        print("This is another derived class programmer")
        
#base class
class land_animal:
    def printing(self):
        print("This animal lives on land.")

class water_animal:
    def display(self):
        print("This animal lives in water.")

class frog(land_animal, water_animal):
    pass

#base class
class A:
    def display(self):
        print("mthod belongs to A")

#derived class
class B(A):
    def display(self):
        print("method belongs to B")
        

class Recursion_practice:
    def __init__(self):
        self.i= 10

    def recursion_test(self, x, y):
        if self.i<= 0:
            return 0

        self.i-= 1
        return x + y + self.recursion_test(x, y)


p1= programmer()
p1.display()
p1.printing()
p1.show()

f1= frog()
f1.printing()
f1.display()

b1= B()
b1.display()

recursion_test1= Recursion_practice()
print(recursion_test1.recursion_test(23, 67))