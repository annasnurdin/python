person = {
  "name" : "Annas",
  "car" : "Hyundai",
  "pass" : "wrong"
}

print(person)
print(person["name"])

del person["pass"]
print(person)


for key in person:
  print(key, ":", person[key])

for key, value in person.items():
  print(key, "=", value)

