# comment

'''
multi-line comment
'''

"""
Multi-line comment2
"""

# input and output
'''
name = input('please enter your name')
print('hello ', name)
'''


# variable
'''
a = 1
b = c = d =2
e, f, g = 3, 4, 5

print(a,b,c,d,e,f,g)
'''

# change variable
'''
a = 11
b = 22
c = 33
a,b,c = b,a,a+b+c;
print(a,b,c)
'''

# data type
'''
a = 'hello'
b = 123
c = (1,2)
d = [1,2]
e = {a:1,b:2}
f = {1,2,3}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

# <class 'str'>
# <class 'int'>
# <class 'tuple'>
# <class 'list'>
# <class 'dict'>
# <class 'set'>

'''


# str
'''
a = 'hello'
b = "world"

c = """\
    dafsdfasdfasdf
    dfasdfsdf  
    """

print(a,b,c)

d = a+" d";

e = "ee" "eee"  #true, but not for variable string name 

f = 3*"fff"

print(d,e,f)


print(len(f))


g='12345'
print(g[:])
print(g[0:1])
print(g[1:])
print(g[:3])
print(g[3:3])
print(g[3:5])
print(g[4:6])

h='abcdef'
print(h.capitalize())
print(h.count('a',0,3))
'''


# list
'''
a = ['a','b','c','d']

b = [a,[1,2,3]]

print(a,b)
# ['a', 'b', 'c', 'd'] [['a', 'b', 'c', 'd'], [1, 2, 3]]

c = a+b
print(c)

print(c+b)

print(c*2)

d = c.append("d");
print(c,d)

c.insert(2,"ccc")
print(c)
c.pop()
print(c)
c.remove("d")
print(c)

print(c.index("b"))
d=c[:]

c.clear()
print(c)
print(d)

print([x==1 for x in d])
'''


# if
'''
a = 1
if a>1:
    print(a);
elif a<1:
    print("a<1");

else:
    print("0")
'''


# for
'''
a= [1,2,3,4,5]

for x in a: {
    print(x)
}
'''
    
# while
'''
x=0
while x<5:
    print(a[x])
    x=x+1
'''

#range
'''
x=range(0,5)
print(x)

for i in x:
    print(i)


y = range(0,20,5)
for i in y:
    print(i)


'''



# function
'''
def add_number(num1,num2=1):
    num3=num1+num2

    print("num3 =",num3)
    
    return num3

a = add_number(1,2)
print("a =",a)
'''


# class
'''
class Test:
    a = 123
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()
t.prt()
print(t.a)

print(Test.__dict__)

'''

# class inhret
'''
class Parent:
    parentAttr = 100
    def __init__(self):
        print("require parent __init__ func")

    def parentMethod(self):
        print('require parent method')

    def setAttr(self, attr):
        Parent.parentAttr=attr

    def getAttr(self):
        print ("Parent Attr :", Parent.parentAttr)


class  Child(Parent):
    def __init__(self):
        print("require Child __init__")

    def childMethod(self):
        print("require Child method")


c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

'''