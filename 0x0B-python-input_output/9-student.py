#!/usr/bin/python3
"""define Student Class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """adding new studient
        params:
        first_name = student first name
        last_name = student last name
        age = student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return Student.__dict__
