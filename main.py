print('Hello World!!')
name = "younghoon"
print(name)

a = 10
b = 3.1415927
c = 123455566677700089
d = 5 + 2j

h = True
print(d)
print(type(d))

myList = [1,2,3,4,5]
print(myList)
myList = [1,"2",3.14159,4,5]
ls1 = ['abcd',786,2.23,'lj']
ls2 = [20, 'garden']
'''
This is a comment
'''
print("""hello 
world""")

z='''hello'''
y='hello'
x="""hello"""

print(ls1[2:3])
print(ls1*2)
print(ls1+ls2)

dt = {}
dt['A'] = "all people"
dt[2] = "number two"

print(dt[2])

a = True
print(bool(a==False))
a = None
print(a)
print(type(a))
ls = ["hello", 2, 7.1, 4, "yes", 10]
x = ls[2]
print(x)
print(ls[0])

a = 19
b = 10
print("a//b:",a//b)
print("b in ls", b in ls)


x=3
x*=8/5
print(x)


a=9
b=10
c=4
d="i am string"
e="i am string"
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))

var="Robogarden"
print("var[-5:-2]",var[-5:-2])
print(var[2])
print("""Hi!\rHey Robogarden, my total mark is %f now"""%(12.4))
print(e.capitalize())

count = 0
pattern= 'patt'
arr=['ffafsadasdfmda;dmsa;dsoa;fnewlkwdnkwqndpatt', 'patt', 'pattfhnalsdnsal', 'patt', 'fjoaflasdlasdowqroqnld', 'patt']
#enter your code here

count = arr.count('patt')
print(arr[0])
count = arr[0].count(pattern)
print(count)
count=0
count+=arr[0].count(pattern)
count+=arr[1].count(pattern)
count+=arr[2].count(pattern)
count+=arr[3].count(pattern)
count+=arr[4].count(pattern)
count+=arr[5].count(pattern)
print(f"2+3 is {2+3}")

import math
dir(math)

