try:
  division = 10/0
  number = int(input('Enter a number: '))
  print(number)
except ZeroDivisionError as err: # you can name an error using as 
  print(err)
except ValueError:
  print('Invalid input')