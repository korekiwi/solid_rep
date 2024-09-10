#################################################
"""Task1"""
# O


class Vehicle:
    def __init__(self, max_speed: int):
        self.max_speed = max_speed

    def get_max_speed(self):
        return self.max_speed

    def calculate_speed(self):
        return 0.0


class Bus(Vehicle):
    def calculate_speed(self):
        return self.get_max_speed() * 0.6


class Car(Vehicle):
    def calculate_speed(self):
        return self.get_max_speed() * 0.8


#####################################################
#####################################################
"""Task2"""
# S


class Employee:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def get_emp_info(self):
        return f"name - {self.name} , dob - {self.dob}"


class EmployeeSalaryCalculator:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_net_salary(self):
        tax = int(self.base_salary * 0.25)
        return self.base_salary - tax


#####################################################
#####################################################
"""Task3"""
# L

from abc import ABC, abstractmethod
import math


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass


class SolidGeometryFigure(Figure):
    @abstractmethod
    def volume(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 2 * math.pi * self.radius


class Cube(SolidGeometryFigure):
    def __init__(self, edge):
        self.edge = edge

    def area(self):
        return 6 * self.edge * self.edge

    def volume(self):
        return self.edge * self.edge * self.edge


#####################################################
#####################################################
"""Task4"""
# I


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


class Square:
    def __init__(self, side):
        self.side = side

    def set_side(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


#####################################################
