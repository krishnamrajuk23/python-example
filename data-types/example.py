print("Hello world");
my_string = "abcdefghij";
print(my_string[3:6]);
print(my_string[::2]);
# print(2 + '3'); // Error 
# print(2 - '3') //Error

name = "Jhon";
age = 30;
print("My name is {n}".format(n = name));
print("My name is {n} and age is {a}".format(n=name, a = age));
print("My name is {} and age is {}".format(name,age));

#version 3.6 format method changed to f
print(f"My name is {name} and age is {age}")


#Dictionaries
print('-------Dictionaries--------')
my_dict = {'apple': 2, 'orange': 3}
print(len(my_dict))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())  # items return array of tuples format
my_dict['apple'] = 10
print(my_dict['apple'])


#Tuples
print('-------Tuples--------')
myTuples = (1, 2, 3)
print(len(myTuples))
#print(len(myTuples[1]))  # throw error
