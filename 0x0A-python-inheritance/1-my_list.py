#!/usr/bin/python3
'''define Mylist Class'''


class MyList(list):
    """invoking from parent class"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
