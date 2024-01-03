# created a class named Person which has name and age as the attributes in it
# and creating the greetings with the help of the name and age with the method in the class
# calling the class with objects from outside the class
class Person:
    def __init__(self,Name,Age) -> None:
        self.Name=Name
        self.Age=Age
        
    def greeting(self):
        print(f"Hello, I am {self.Name} and I am {self.Age} years old.")
    
user=Person("Guru",21)
user.greeting()

# Creating the Class named Shape and creating the method area and 
# creating the subclass of circle and rectangle with Shape class as a Parent class
# and printing the area of the circle and the rectangle with the help of area method 
class Shape:
    
    def area(self):
        pass
    
class Circle(Shape):
    
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return (22*self.radius*self.radius)/7
    
class Rectangle(Shape):
    
    def __init__(self,base,length):
        self.base=base
        self.length=length
        
    def area(self):
        return (self.base*self.length)/2

area_circle=Circle(int(input("Enter the radius of the Circle: ")))
print(f"The Area of the Circle is : {area_circle.area():.2f}")

values = input("Enter the base and length of the rectangle separated by a comma: ")

# Split the input values using the comma as a delimiter
base, length = map(int, values.split(','))

area_rectangle=Rectangle(base,length)
print(f"The Area of the Rectangle is : {area_rectangle.area()}")