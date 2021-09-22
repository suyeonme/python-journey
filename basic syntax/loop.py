# while loop 
i = 1
while i <= 10:
  print(i)
  i += 1

# for loop 
for letter in 'Suyeon':
  print(letter)

names = ['Suyeon', 'Hanna', 'Sarang']
for name in names:
  print(name)

for index in range(10):
  print(index)

for index in range(3, 11):
  print(index)

for index in range(len(names)):
  print(index)

# nested for loop 
number_grid = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0],
]

for row in number_grid:
  for col in row:
    print(col)