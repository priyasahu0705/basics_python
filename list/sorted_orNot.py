def CheckSorted(num):
  for i in range(1,len(num)):
    if num[i]>num[i-1]:
      pass
    else:
      return False
  return True
  
print(CheckSorted([4,8,6,40]))
print(CheckSorted([4,8,16,45,60]))


""""
def CheckSorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True
print(CheckSorted([4,8,6,40]))
print(CheckSorted([4,8,16,45,60]))
"""


  