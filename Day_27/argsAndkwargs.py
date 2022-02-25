# args takes any number of parameters in function not a fixed size.

def add(*args):                              
    print(type(args))            
    add=0
    for n in args:
        add+=n 
    return add


addition=add(1,2,3,4)
print(addition)


# kwargs allows any number of keyword arguments

def calculate(n,**kwargs):                        
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["add"])
    print(n)
    n+=kwargs["add"]
    print(n)

calculate(2,add=3,multiply=5)
