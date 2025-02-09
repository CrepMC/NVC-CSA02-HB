# Python Basics

#### Print: Script show in screen.
```python
print("hello")
print(1000)
print(True)
```
#### Comment script: #
- To explain the usage or algorithm of a script
- To disable a script
Variable:
- Consider as container of value
- No need to create just add value to variable in Python
```C++
count = 10;
```

#### Basic data:
- int: 1, -2
- float: 4.5, 5.3
- string: "haha"
- boolean: True, False

```python
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #get integer part
print(a%b)  #take the remainder
print(a**b) #Exponent
```

#### Relative algorithm
```python
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)
print(a == b)
print(a !== b)
```

#### Logic algorithm
```python
a = 10
b = 4
c = 7
d = 1000
print(a < b and c >= d)
print(a < b or c >= d)
print(a > b and c <= d)
print(a > b or c <= d)
print(a < b and c <= d)
print(a < b or c <= d)
print(a > b and c >= d)
print(a > b or c >= d)
```

#### Turn branch structure
```python
if a > b:
    print("a is greater")
elif b > a
    print("b is greater")
else:
    print("a and b equal")
```

#### Repeat structure
```javascript
for (let i = 0; i < 10; i++) {
    console.log(i)
}
```
```python
for i in range(10):
    print(i)
# 0 1 2 3 4 5 6 7 8 9 10

# While repeat circle - Do not now the number of the repeat time
count = 0
while count < 10
 print ("Hello")
 count = count + 1
```

#### Details of range() function
- Range function create a list of integer
- There are 3 script of range function, overview script: range(start, end, step)
- In case of 1 parameter: range(a, b): give back list [1, 2, 3, ..., n-1]
- In case of 2 parameter: range(a, b): give back list [a, a+1, a+2, ..., b-1]
- In case of 3 parameter: range(a, b): give back list [a, a+x, a+2x, ..., (before b)] 
Example:
range(1, 50, 13): [1, 14, 27, 40]