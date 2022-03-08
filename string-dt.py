
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


# ======= Error ===== #
# To run this file comment this section
#my_string[5] = 'a'  # error => 'str' object does not support item assignment
#del my_string[1]      # error => 'str' object doesn't support item deletion

# ======= Concatenation of two or more string ===== #
str1 = "Hello"
str2 = "world"
print("concate two string", str1 + str2)
print("concate with number", str1 * 3)  # output: HelloHelloHello

#---want to concatenate strings in different lines, we can use parentheses ---#
# two string literals together
# o/p: concatenate strings bind things
print("concatenate strings", 'bind ' 'things')

# using parentheses
print("concatenate strings with parentheses", ('hello'
                                               'world'))  # o/p: concatenate strings with parentheses hello world

#-----Iterating through a string----#
count = 0
for str in my_string:
    if(str == 'r'):
      count += 1
print(count, "letter 'r' found")
