num =[12,32,54,67,98,100]
largest=num[0]
second_largest=num[0]
for i in num:
  if i > largest:
    second_largest=largest
    largest=i
  elif i>second_largest and i!=largest:
    second_largest=i
print(second_largest)