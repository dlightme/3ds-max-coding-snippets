# -*- coding: utf-8 -*-
"""
Created on Wed May  4 18:06:11 2022

@author: w.haak
"""

from dataclasses import dataclass, field

@dataclass
class Person:
    sort_index: int = field(init=False)
    name: str
    job: str
    age: int
    #default value
    strength: int = 100
    
    def __post_init__(self):
        self.sort_index = self.strength
    
    def __str__(self):
        return f'{self.name},{self.job} ({self.age})'
    
Person1 = Person("Gerald", "foo", 32, 99)
Person2 = Person("Jennie", "bar", 28)
Person3 = Person("Gerald", "foo", 32, 99)

print(Person1)
print(Person1==Person3) 

# this is using the sort_index: (not working)
print(Person1 > Person2)

