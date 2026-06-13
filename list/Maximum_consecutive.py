
def maximunConsecutive(num):
  max1=1
  count =0
  for i in num:
    if i==1:
      count+=1
      max1=max(max1,count)
    else:
      count=0
  return max1
print(maximunConsecutive([1,1,2,1,1,1,4,1,1,1,1,1,1]))