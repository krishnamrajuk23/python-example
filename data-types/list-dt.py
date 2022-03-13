#========== List ============#

my_string = "hello"
myList = []
for letter in my_string:
    myList.append(letter)

print("Get list elements", myList)

#-------- short hand of above code --------#

elements = [letter for letter in my_string]
# o/p: same as print statement one
print("short hand code of list assignment", elements)

myList = [x for x in range(0, 10) if x % 2 == 0]
print("myList values", myList)  # opt: [0,2,4,6,8]

myList = [x**2 for x in range(0, 10) if x % 2 == 0]
print("myList values", myList)  # opt: [0,4,16,36,64]



