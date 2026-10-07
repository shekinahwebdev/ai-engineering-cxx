class Vehicle:
    def __init__(self,name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


vehicle1 = Vehicle("Tesla Model S", 250, 18)
print(f"Vehicle Name: {vehicle1.name}, Speed: {vehicle1.max_speed}, Mileage: {vehicle1.mileage}")


class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width


    # instance method 
    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * self.width + 2 * self.length


rect = Rectangle(10,4)
print(f"Area = {rect.area()}")
print(f"Perimeter = {rect.perimeter()}")


class Student:
    def __init__(self,name, marks = []):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)


s1 = Student("Alice", [85, 90, 78, 92, 88])
print(f"{s1.name}'s Average Grade: {s1.average()}")


