monthConversions = {
  'Jan': 'January',
  'Feb': 'February',
  'Mar': 'March',
  1: 'First'
}

print(monthConversions['Jan'])
print(monthConversions.get('Mar'))
print(monthConversions.get('Test', 'Not a valid key')) # default value 


# key and value pair