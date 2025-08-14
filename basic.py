1+1

import os  #module in python 
os.getcwd()

4*6
22/7

a=5
print(a)
a+a

3==3
3!=3

#list - (ordered, mutable (can add, modify , remove), allows duplicates) ordered means when you add element it will be at end of list
x=['a','b',2]
print(x)
y=[3,2,5]
sorted(y)
reversed(y)
print(sorted(y))
print(list(reversed(sorted(y))))
x.count('a')
len(x)
x[0] =20  #modify
x.append('c') #add
del x[1]  #remove


#tuple (ordered, immutable (cannot add, modify , remove), allows duplicates)
t=(1,2,3)
t[0]
sorted(t)
t.append(4) #error
t[0]=10 #error
del t[0] #error

#dictionary {'key':'value'} (unordered, Python 3.7+: insertion ordered, unique keys)
a={'a':1, 'b':2, 'c':3}
a.keys()
a.values()
a['a']

b={1: 10, 2:20,3:30}
b[1]

#set (unordered, mutable, unique elements only)
s={1,2,3}
s.add(4)
s.remove(2)

#function

def fun():
    print("Hello")

fun()

class Car:
    def __init__(self,make,model,year):
        self._make = make #protected attribute
        self.__model = model #private attribute
        self.year = year #public attribute

    def get_make(self):
        return self._make
    
    def set_model(self,model):
        self.__model = model

    def get_model(self):
        return self.__model
    

my_car = Car('Tesla', 'Model S', 2020)
print(my_car.get_make())  # Accessing protected attribute
