import math

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):

        return a * b

    def divide(self, a, b):

        if b == 0:

            raise ValueError("Cannot divide by zero.")

        return a / b
    def calculate_rectangle_area(self, length, width):

        return length * width
    def calculate_circle_area(self, radius):

        return math.pi * radius ** 2


# TODO: Implement the following function to calculate the square root of a number.

    def square_root(self, x):

        return math.sqrt(x)

# You need to uncomment the above function and complete its implementation to add the square root feature.

if __name__ == "__main__":

    calculator = Calculator()

    num1 = 16

    num2 = 4

    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")

    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}") 
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")

    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

#TODO: Uncomment and test the square root feature.

    num3 = 25

    print(f"The square root of {num3} = {calculator.square_root(num3)}")
# TODO: Implement the feature to calculate the area of a rectangle # 
    length = 10

    width = 6

    print(f"The area of the rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length, width)}")
# TODO: Implement the feature to calculate the area of a circle

    radius = 5

    print(f"The area of the circle with radius {radius} ={calculator.calculate_circle_area(radius)}")
