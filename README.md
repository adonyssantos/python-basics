# Python Programing Language

## What is Python?

Python is a programming language. It is a high-level, interpreted, object-oriented, and dynamic programming language. Python is designed to be highly readable. It is also easy to learn.

## Keep in mind

1. Python is case sensitive language. `print` is not `Print`.
2. Spacing is important. There will be no error if you do not use the correct indentation.
3. Use error messages to help you learn.

**Print function**

```python
print("Hello World") # Hello World
print(10) # 10
print(8 + 1.5) # 9.5
print(True) # True
print(None) # None
```

`print` function is used to print the output.

## Arithmetic Operators

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Mod (the remainder after dividing)
- `**` Exponentiation (note that `^` does not do this operation, as you might have seen in other languages)
- `//` Divides and rounds down to the nearest integer

### Example

```python
print(3 + 5) # 8
print(1 + 2 + 3 * 3) # 12
print(3 ** 2) # 9
print(9 % 2) # 1
print(10 // 3) # 3
```

## Variables and Assignment Operators

Variables are used all the time in Python!

### Example

```python
x = 10
y = 20

print(x + y) # 30
print(x - y) # -10
print(x * y) # 200
```

or

```python
x, y = 10, 20

print(x + y) # 30
print(x - y) # -10
print(x * y) # 200
```

### Variable names rules

1. Variable names cannot start with a number.
2. Variable names cannot contain spaces.
3. Variable names cannot contain special characters.
4. Variable names cannot contain the programing language reserved words.
5. Variable name can contain letters, numbers, and underscores.
6. Variable names can be in camel case, snake case, or even kebab case.
7. Variable names can be descriptive.

## Data Types in Python

- `int`: Integer
- `float`: Floating point number
- `bool`: Boolean
- `str`: String
- `list`: List
- `dict`: Dictionary

### Example

```python
x = 10 # int
y = 20.5 # float
z = True # bool
a = "Hello" # str
b = [1, 2, 3] # list
c = {"name": "Adonys", "age": 18} # dict
```

## String methods

The string methods are used to manipulate strings.

### isLower()

```python
print("Hello".isLower()) # False
print("hello".isLower()) # True
```

### isUpper()

```python
print("Hello".isUpper()) # False
print("HELLO".isUpper()) # True
```

### format()

```python
print("Hello {0}".format("World")) # Hello World
print("Hello {0}".format(10)) # Hello 10
print("Hello {0}".format(10.5)) # Hello 10.5
print("Hello {0}".format(True)) # Hello True
print("Hello {0}".format(None)) # Hello None
```

### split()

```python
print("Hello World".split()) # ['Hello', 'World']
print("Hello World".split("o")) # ['Hell', ' Wrd']
```
