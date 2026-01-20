index = 1

while index <= 100:
  if index % 15 == 0:
    print("fizzbuzz: ", index)
  elif index % 3 == 0:
    print("fizz: ", index)
  elif index % 5 == 0:
    print("buzz: ", index)
  else:
    print(index)
  
  index += 1

print("DONE")