num=[4,5,9,7,12,45]
# slicing
print(num[::-1])
# with range Method
for i in range(len(num)-1,-1,-1):
  print(num[i])
# with new list
result=[]
for i in range(len(num)-1,-1,-1):
    result.append(num[i])
print(result)