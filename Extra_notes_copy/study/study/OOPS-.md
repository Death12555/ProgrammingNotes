- Object- It is a collection of data and its functionality. Its an instance of a class.
- Class- Blueprint/Template to create an object. It is the prototype for an object.
- pass is used to pass an empty class.
- In an empty class fields(data) and methods are not present.
- class Test:
    pass

class person:
	def __init__(self, name):
		self.name= name
	def display(self):
		print("hello", self.name)

class student:
	clg= 'xyz' #classvariable
	def __init__(self,  rollno,  name):
	self.name= name
	self.rollno= rollno
	def display(self):
	print("student name:", self.name)
	print("student rollnumber:", self.rollno)
	print("college:", student.clg)
	
if '__name__'=='main':
    p= Test(()
    person1= person()
    print(p)
    person1.display()
    person("amul").display()
    student1= student('xyz001', "amul")
    student1.display()
    student2= student('xyz056', "john")
    student2.display()

Output: <(underscore)(underscore)main(underscore)(underscore).Test object at 0x7f0d70bba8b0>
Here we can see that, object that belongs to class person is created in the main and it is saved in this(0x000001C934EABA20) memory location.

- Methods- These are the functions that belongs to class.
- To define a method we use def followed by method name.
- The first parameter of every method will be self, which is used to refer to the object itself. self is not a keyword, i.e.: We can use any word instead of self but it is recommended to use self.
- __init__ method is used to initialize the object.
- e.g.: in above example: self.name is used to initialize the object
- We don't need to call this method because when the object is created, it is called automatically.
- self parameter is used to differentiate between the instance variable and local variables.
- instance variables are variables are variables belonging to an object. e.g.: In above example self.name is the instance variable and name( in: = name) is the local variable.
- person("name").display() can also be used to do the same thing.
- Instance variable: The variable that belongs to an object/instance.
- Class variable: The variable that belongs to a class is called the class variable. i.e. The variable that belongs to all the objects in the class. This implies that this property is same for all the objects of this class.
- To access class variable, we need its class name along with its class variable. e.g.: In the above example student.clg is used to access class variable.
- We can even use some other variable name like myself, displayself etc. instead of self.
- In Python, the `@staticmethod` decorator is used to define a static method within a class. A static method is a method that belongs to the class rather than an instance of the class. It doesn't have access to the instance or its attributes and doesn't modify them. Instead, it is bound to the class and can be called on the class itself.

Here's an example to illustrate the use of `@staticmethod`:
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# Using static methods
result_sum = MathOperations.add(3, 5)
result_product = MathOperations.multiply(3, 5)

print(result_sum)       # Output: 8
print(result_product)   # Output: 15

- In this example, `add` and `multiply` are static methods. They are defined using the `@staticmethod` decorator, and you can call them on the class itself (`MathOperations.add(3, 5)`) without creating an instance of the class.

Static methods are useful when a method doesn't need access to the instance or its attributes, and it makes sense for the method to be associated with the class rather than an instance.

---------

## Fundamentals features of Object Oriented Programming:
1.  **Inheritance**: Inheritance allows a class to inherit the properties of another class. Or we can say, we can create a new class by using the properties of already existing class. Here, The newly created class is called derived class or child class and the already existing class is called the base class or parent class.

	![[Screenshot 2023-12-05 at 4.15.38 PM.png]]

	From the above example we can say that the newly created class will contain properties(Feature 1 and Feature 2) as well as newly created methods(Feature 3)

	![[Screenshot 2023-12-05 at 4.19.36 PM.png]]

	To use methods from the base class  in a derived class we need to pass/mention the base class name as argument in derived class.

	![[Screenshot 2023-12-05 at 4.25.21 PM.png]]

	If we don't use inheritance then compiler will throw: AttributeError: 'dog' object has no attribute 'eating'.

	![[Screenshot 2023-12-05 at 4.28.26 PM.png]]

	In inheritance, derived class can inherit methods and variables of/from the base class.
	The example above was an example of Single-Level Inheritance(Single Base Class and Single Derived Class).

2. MultiLevel Inheritance: ![[Screenshot 2023-12-05 at 4.33.24 PM.png]]

	Here, we derive a class(Derived Class 1) from Base Class and from this Derived Class 1 we can derive another class(Derived Class 2), as we can see there are multiple levels, thats why it is called MultiLevel inheritance.

	Example: ![[Screenshot 2023-12-05 at 4.38.29 PM.png]]

	![[Screenshot 2023-12-05 at 4.39.00 PM.png]]

	Here, person is the base class, and employee is derived from the base class person, and the programmer is derived from the derived class employee.

3.  Multiple Inheritance:
	![[Screenshot 2023-12-05 at 4.47.51 PM.png]]

	in Multiple Inheritance, there'll be more than one base class. If a new class is derived by more than one base class, then it is called as multiple inheritance.

	Example:
	![[Screenshot 2023-12-05 at 4.50.35 PM.png]]

	In the above examples, specifically for class frog, there is land class for land living animals and water for water class for water living class and frog belongs to both since it is land and water living. So it is derived from both.

	  For child class, it contains DNA from mother as well as father base class so it is derived from both.
	  
	  Example:![[Screenshot 2023-12-05 at 4.54.28 PM.png]]

4.  Method Overriding:	
	![[Screenshot 2023-12-05 at 5.02.16 PM.png]]
	
	If we want different implementation of class A for class B in above example, i.e.: We want the same method but different method body in the derived class. Then we can do that by overriding the method in the derived class. To do that we just need to define that method(here, display) in the derived class(Change the method body).
	
	![[Screenshot 2023-12-05 at 5.10.47 PM.png]]
	
	The ability of a class to change the implementation of method provided by one of its ancestors or we can change the implementation of a method in the derived class which is provided by its base class. To override that method we need to define that method in the derived class with the same name.

5. Encapsulation:
	Restricting access to variables and and methods. we do this to prevent the data from being modified by other methods and classes not related to the 2 that are necessary for each other.
	Till now we have been using public methods and public variables(i.e.: We can access them outside the class too).

	Example:
	![[Screenshot 2023-12-05 at 6.12.56 PM.png]]
	
	![[Screenshot 2023-12-05 at 6.13.23 PM.png]]

	But private methods are not accessible outside the class.
	
	There are 2 types of access specifiers:
	i) Private 
	ii) Public

	In object-oriented programming, access modifiers are keywords that determine the visibility and accessibility of class members (attributes and methods). The two primary access modifiers in many programming languages, including Python, are "public" and "private."

	i ) **Public:**    
	    - **Visibility:** Public members are accessible from outside the class.
	    - **Keyword:** In Python, members are public by default, meaning that you don't explicitly declare them with a keyword.
	    - **Example:**
			class MyClass:
				def __init__(self, x):
				     self.x = x  # x is a public attribute
				def print_x(self):
				     print(self.x)  # print_x is a public method
	ii)  **Private:**
	    - **Visibility:** Private members are not accessible from outside the class.
	    - **Keyword:** In Python, you can indicate that a member is private by prefixing its name with a double underscore (`__`).
	    - **Example:**
		    class MyClass:
			 def __init__(self, x):
				 self.__x = x  # __x is a private attribute
			def __print_x(self):
				print(self.__x)  # __print_x is a private method
	iii) Accessing Private Members:
		While you generally can't access private members directly from outside the class, Python doesn't enforce strict privacy, and you can still access them with name mangling (`_ClassName__member`). However, it's considered bad practice to do so, and it may lead to unexpected behavior.
		It's important to note that these access modifiers provide a way to express intent and convention rather than strict enforcement. In Python, for example, there's no strict enforcement of access control, and the convention is to treat members with a single leading underscore (`_`) as "protected" (intended for internal use) and members with a double leading underscore (`__`) as "private."
		Here's an example illustrating public and private members:
		class Example:
			def __init__(self):
				self.public_member = "I'm public"
				self.__private_member = "I'm private"
			def public_method(self):
				print("Public method")
			def __private_method(self):
				print("Private method")
	# Usage
	obj = Example()
	print(obj.public_member)     # Accessing public member
	obj.public_method()          # Calling public method
	# Attempting to access private member/method will result in an AttributeError
	# print(obj.__private_member)  # This will raise an AttributeError
	# obj.__private_method()       # This will raise an AttributeError

	In practice, it's often recommended to use the convention of a single leading underscore for "protected" members and a double leading underscore for "private" members.

	Example:
	![[Screenshot 2023-12-05 at 6.41.28 PM.png]]

	Here, the __updatesoftware() is private method and we are calling this inside the class.
	
	Output:
	updating software
	driving

	The output is so because whenever we create an object, it will automatically call the initialising method. In the initialisation method, we called private method __updatesoftware(), so it will print that message first. After which we called the drive method which will print "driving". Here we can't call this __updatesoftware() outside the class, if we do it'll give an error(AttributeError: 'car' has no attribute '__updatesoftware').
	
	Private variables can be modified only inside the class methods, we can't modify the variables outside the class.
	 
	 Example:
	 ![[Screenshot 2023-12-05 at 6.54.27 PM.png]]
	
	![[Screenshot 2023-12-05 at 6.55.50 PM.png]]

	Here we can't change the value of __maxspeed because it is a private variable.

6. Polymorphism:
	Here, poly means many and morphing means forms.
	So polymorphism means many forms.
	Polymorphism means the ability of an object to adopt the code to the type of data processing.
	Polymorphism helps us to define an action regardless of the type of object.
	It is nothing but a method which behaves differently for different objects.

	Example:
	![[Screenshot 2023-12-05 at 7.10.10 PM.png]]

	![[Screenshot 2023-12-06 at 1.02.54 PM.png]]

7. Function Overloading:
	Function overloading is a programming concept where a class or module can provide multiple functions or methods with the same name but different parameters or method signatures. This allows a programmer to use the same function or method name for operations that conceptually perform a similar task but require different types or numbers of inputs.

	In languages that support function overloading, such as C++, Java, and others, the compiler or runtime environment is capable of distinguishing between different versions of a function based on the number and types of arguments provided. This allows developers to create more readable and expressive code by using the same function name for logically related operations.

	Key points about function overloading:
	1. **Same Name, Different Signatures:**
	    - Multiple functions share the same name.
	    - Each function has a unique signature, which includes the number and types of its parameters.
	
	2. **Compile-Time or Run-Time Resolution:**
	     - In some languages like C++, function overloading is resolved at compile time. The compiler determines which function to call based on the provided arguments.
	     - In other languages like Python, function overloading is achieved through default parameter values and variable-length argument lists, and the resolution occurs at runtime.
	
	3. **Improved Readability and Maintainability:**
		- Function overloading enhances code readability by allowing developers to use a single, consistent name for similar operations.
		- It makes the code more maintainable, as changes to the implementation of a task can be done in one place without affecting other calls to the function.
	4. **Example in Python:**
			class MathOperations:
			    def add(self, a, b):
			        return a + b
			    def add(self, a, b, c):
			        return a + b + c
			# Usage
			math_ops = MathOperations()
			result1 = math_ops.add(1, 2)          # Calls the first version of add
			result2 = math_ops.add(1, 2, 3)       # Calls the second version of add
		- Note: In Python, the latest definition of a method with a particular name and within the same scope overrides the previous ones.
    

	It's important to check the documentation or specifications of the programming language being used to understand how function overloading is implemented in that specific language.
	

	![[Screenshot 2023-12-06 at 2.01.26 PM.png]]

	Class is just used to define a new datatype(object).

Constructors:
	Constructor is a special member function, with same name as the class.
	It is used to initialise the objects of its class. It is automatically invoked. whenever an object is created. 
	When we create a constructor it has no return type/return type is not important, as opposed to other member functions whose return type needs to be given.
	It has the same name as the class in languages like C++.

In Python:
	Here, __init__() is a special method that is used to create constructors.
	It is a dunder method.
	![[Screenshot 2023-12-15 at 6.21.06 PM.png]
	
Types of Constructors:
	1. Default Constructor: The constructor that doesn't accept any parameters are called default constructors.
	2.  Parameterised Constructor: When the constructor accepts arguments along with itself('self' arguement). These arguments can be used inside the class to assign values to the data members.

Properties/Characteristics:
	1. It should be declared in the public section of the class.
	2.  They are invoked whenever the object is created. Whenever the object is created it also runs for it.
	3.  They do not have return types, therefore they can't return values.
	4.  It can have default values.
	5.  We can't refer to their address.

Main in python:
	The `if __name__ == '__main__':` block in Python is a common idiom used to check whether the Python script is being run as the main program or if it is being imported as a module into another script. It helps to distinguish between the script being used as the main program or being imported as a module in another program.

Here's how it works:

1. When a Python script is executed, the interpreter assigns the special variable `__name__` a value of `'__main__'` if the script is the main program being run.

2. If the script is being imported as a module into another script, then `__name__` is set to the name of the module (not `'__main__'`).

	By using `if __name__ == '__main__':`, you can include code that should only run when the script is executed directly, not when it's imported as a module. This is useful for creating reusable modules where you might have some code for testing or running specific tasks that should only be executed when the script is the main program.

	For example:

```python
def some_function():
    print("This function can be reused in other scripts.")

if __name__ == '__main__':
    # Code inside this block will only run if the script is executed directly
    print("This will only run when the script is the main program.")
    some_function()
```

In the above example, `some_function()` can be imported and used in other scripts without triggering the code inside the `if __name__ == '__main__':` block. The block is mainly for code that you want to run when the script is executed directly.

Python concepts and function cheatsheet:
	https://www.codewithharry.com/blogpost/python-cheatsheet/