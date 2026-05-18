Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#swapping
a=6
b=7
a,b=b,a
print(a,b)
7 6
#method 2
temp=a
a=b
b=temp
print(a,b)
6 7
a=9
b=7
temp=a
a=b
b=temp
print(a,b)
7 9
#method 3
a=8
b=9
a=a-b
b=a-b
print(a,b)
-1 -10
a=6
b=0
a=a=b
b=a-b
a=a-b
print(a,b)
0 0
a=6
b=0
a=a+b
b=a-b
a=a-b
print(a,b)
0 6
#method 4
a=9
b=0
a,b=b,a
print("a=%d,b=%d" %(a,b))
a=0,b=9
#strings
a=9
b=8
a,b=b,a
print("a=%s,b=%s" %(a,b))
a=8,b=9
a="sreshta"
b="divya"
a,b=b,a
print("a=%s,b=%s" %(a,b))
a=divya,b=sreshta
a=8
b=6
print("a=%d,b=%d" %(a,b))
a=8,b=6
a=8.0
b=9.8
a=a,b
a=9.8
b=7.0
a,b=b,a
ptint("a=%f,b=%f" %(a,b))
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    ptint("a=%f,b=%f" %(a,b))
NameError: name 'ptint' is not defined. Did you mean: 'print'?
print("a=%f,b=%f" %(a,b))
a=7.000000,b=9.800000
print("a=%2f,b=%3f" %(a,b))
a=7.000000,b=9.800000
print("a=%.2f,b=%.3f" %(a,b))
a=7.00,b=9.800
ptint("a=%d,b=%d" %(a,b))
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    ptint("a=%d,b=%d" %(a,b))
NameError: name 'ptint' is not defined. Did you mean: 'print'?
print("a=%f,b=%f" %(a,b))
a=7.000000,b=9.800000
print("a=%d,b=%d" %(a,b))
a=7,b=9
#list
#append
a=[2,4.5,"python",True]
print(a)
[2, 4.5, 'python', True]
type(a)
<class 'list'>
a=9
prin(a)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    prin(a)
NameError: name 'prin' is not defined. Did you mean: 'print'?
a=8
type(a)
<class 'int'>
a=[8]
type(a)
<class 'list'>
#append
a=["python","java","sql","html"]
a.append("ds","ml")
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a.append("ds","ml")
TypeError: list.append() takes exactly one argument (2 given)
a=["python","html"]
a.append(["ml","ds"])
print(a)
['python', 'html', ['ml', 'ds']]
#extend
a.extend(["ds","ml"])
print(a)
['python', 'html', ['ml', 'ds'], 'ds', 'ml']
a=["hello","bye"]
a.extend(["divya","har"])
print(a)
['hello', 'bye', 'divya', 'har']
a=["python","java"]
a.insert(1,"c++")
print(a)
['python', 'c++', 'java']
#index
a=["sreshta","divya"]
a.index("sreshta")
0
a.copy()
['sreshta', 'divya']
b=a.copy()
b
['sreshta', 'divya']
a.clear()
a
[]
a=[]
a.append("mahima rani","raju")
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a.append("mahima rani","raju")
TypeError: list.append() takes exactly one argument (2 given)
a.append("jesus")
a
['jesus']
a=["apple","grapes","banana","watermillon"]
a.sort()
a
['apple', 'banana', 'grapes', 'watermillon']
a=[7,6987,88,890,4578,69,680,678]
a.sort()
a
[7, 69, 88, 678, 680, 890, 4578, 6987]
#duplicate
a=[7.800,678]
a=[7,8,9,9,0]
a
[7, 8, 9, 9, 0]
#reverse
a=["hello",900]
a.reverse()
a
[900, 'hello']
a=["sreshta","divya"]
a.reverse()
a
['divya', 'sreshta']
a=[7,9,0,8,9,9,0,0,6,5]
a.reverse()
a
[5, 6, 0, 0, 9, 9, 8, 0, 9, 7]
a=["sreshta",56,9.0,True,False]
a
['sreshta', 56, 9.0, True, False]
a.sort()
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
a.reverse()
a
[False, True, 9.0, 56, 'sreshta']
a=[0,9,8]
a.pop()
8
a
[0, 9]
a.pop(9)
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    a.pop(9)
IndexError: pop index out of range
a.pop(0)
0
#remove
a=[0,9,8]
a.remove(8)
a
[0, 9]
a=["sreshta","divya"]
a.pop(0)
'sreshta'
a
['divya']
a.remove("divya")
a
[]
#count()
a=[5,8,9,8,9,0]
>>> a.count(9)
2
>>> #len
>>> a="sreshta"
>>> len(a)
7
>>> b=["sreshta"]
>>> len(b)
1
>>> #tuple
>>> a=(7,7.0,"sreshta",True,8+9j)
>>> a
(7, 7.0, 'sreshta', True, (8+9j))
>>> type(a)
<class 'tuple'>
>>> a.count("sreshta")
1
>>> len(a)
5
>>> len("sreshta)
...     
SyntaxError: unterminated string literal (detected at line 1)
>>> len("sreshta")
...     
7
>>> a.index("sreshta")
...     
2
>>> #task
...     
