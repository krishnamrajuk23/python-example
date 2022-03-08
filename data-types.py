# Data Types
# Integer                 - int
# string                  - str
# floating point          - float
# List                    - list  [val1, val2]
# Dictionaries            - dict  {key: value}
# Tuples                  - tup - ordered immutable sequence of objects (10, "hello", true)
# Sets                    - set - unordered unique objects {"a", "b"}
# Booleans                - logical values true/false

#====== String ===========#

my_string = "programming"

# Access first character from string
print("first character ", my_string[0])

# Access last character from string
print("last character ", my_string[-1])

# slicing 1st to 5th character
print("between character ", my_string[1:5])

# slicing 3rd to 2nd last character
print("between character ", my_string[3:-2])

# start:stop:steps
reverseStr = my_string[::-1]
print("reverse string ", reverseStr)


#======= Error =====#
my_string[5] = 'a'  # error => 'str' object does not support item assignment
del my_string[1]      # error => 'str' object doesn't support item deletion
