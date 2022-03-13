# remove negative values and split odd value as even number comma one (5 - 4,1)
# keep even at it is

def logic_fun(lists):
  finalResult = []
  for list in lists:
      if(list > -1):
        if(list % 2 == 0):
          finalResult.append(list)
        else:
          finalResult.append(list-1)
          finalResult.append(1)
  return finalResult


getListOfLogicNumber = logic_fun([5, 2, 7, -4, 6, -3])
print(getListOfLogicNumber)


def player_guess():
  guess = ''
  while guess not in ['0', '1', '2']:
    guess = input('pick a number:')

  return int(guess)


def check_guess(my_list, guess):
  if my_list[guess] == '0':
    print('Correct!')
  else:
    print('Wrong Guess!!')
    print(my_list)


#----multiple function ----#
my_list = ['', '0', '']

#Get Player guess
guess = player_guess()

#check the answer
check_guess(my_list, guess)
