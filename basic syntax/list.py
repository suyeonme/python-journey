names = ['Suyeon', 'Suyeon', 'Hanna', 'Sarang', 'Crystal']
numbers = [1,2,3,4,5]

print(names[-2]) # backward 
print(names[1:]) # from index to the end  
print(names[1:3]) # [start:end]


# List functions 
names.extend(numbers) # add a list to the list 
names.append("John") # add an item to the end  
names.pop() 
names.insert(1, "John") # (index, value)
names.remove("John") 
names.clear() # remove all items of a list

names.count('Suyeon')
numbers.sort() 
numbers.reverse() 
numbers2 = numbers.copy() 

# 2D list 
number_grid = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0],
]
print(number_grid[0][0])