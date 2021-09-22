text_file = open('./resources/employee.txt', 'r')
print(text_file.readable())
print(text_file.read())
print(text_file.readline())
print(text_file.readlines()) # put lines to an array

for line in text_file.readlines():
  print(line)

text_file.close() 

# r: Read
# w: Write
# a: Append (end to the file)
# r+: Read and Write

