#------> first question
def convert(number):
    while number > 0:
            digit = number % 10
            print(digit)
            number = number//10
    else:
          print('invalid')
convert(1011)