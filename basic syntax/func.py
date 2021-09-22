def exponent_num(base_num, pow_num):
  res = 1
  for index in range(pow_num):
    res = res * base_num
  return res

print(exponent_num(3, 2))