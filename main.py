# -*- coding: utf-8 -*-
"""
Created on Sat Jan  3 17:31:23 2026

@author: chara
"""

print("om gnaesh please help me that i do well")


class A:
    def __init__(self):
        self.value = 100

    def set_value(self, v: int):
        self.value = v
        
    def get_value(self):
        return self.value
    
    
    
a_object = A()
a_object.value

a_object.set_value(10)
    

def check(a):
    a.append("l")
    print(a)
     
    
b=["a"]

check(b)


a=["11"]
new_list = a + ["l"]
id(new_list)

c=new_list.append('o')



a=5;b=2.3

isinstance(a,(float,int))



from pandas import  DataFrame

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Delhi", "Mumbai", "Bangalore"]
}

df = DataFrame(data)
print(df)



a = [1,2,3]

b= a

c=list(a)
a==b

id(a)




a = ((91,2,3),(5,6,7,8))

b= a

c=list(a)


a=10
id(a)

a is 

a=[1,2,3]
b=list(a)
id(None)
a is b
a == b


a =None
id(a)



a is None 

a=[]

if a:
    print("Has data")
    
if not a:
    print("Empty list")
    
    
    
    
a = None 
a is None


















