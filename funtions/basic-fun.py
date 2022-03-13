def say_hello():
  print("hello world")


say_hello()


def add_num(num1, num2):
  print(f'sum of number is {num1+num2}')


add_num(10, 20)


def getName(name='raju'):
  return f'My name is {name}'


who_are_you = getName()  # default argument assignment
who_are_you = getName('Krishna')
print(who_are_you)
