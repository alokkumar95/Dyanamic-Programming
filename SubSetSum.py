""" Subset Sum Problem
arr=[2,3,7,8,10]
sum=11
Check if a subset exists whose sum equal to 11 then return true else false
"""

import pprint
pp=pprint.PrettyPrinter()

def subSetSum(arr,sum1):
  n=len(arr)

  t=[[False] * (sum1+1) for _ in range(n+1)]

  """ When there is no element in arr then sum can't be possible out of that element except zero sum"""
  for j in range(sum1+1):
    t[0][j]=False 
  
  """ When sum is zero and there are elements in arr then empty element can make sum equal to zero"""
  for i in range(n+1):
    t[i][0]=True

  for i in range(1,n+1):
    for j in range(1,sum1+1):
      if arr[i-1]<=j:
        t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
      else:
        t[i][j]=t[i-1][j]

  print("Top down Matrix")
  for item in t:
    print(item)
  return t[n][sum1]

arr=[2,3,7,8,10]
sum1=11
print("\nIs a subset exist whose sum equal to {} ? {}".format(sum1,subSetSum(arr,sum1)))

"""
Output
Top down Matrix
[True, False, False, False, False, False, False, False, False, False, False, False]
[True, False, True, False, False, False, False, False, False, False, False, False]
[True, False, True, True, False, True, False, False, False, False, False, False]
[True, False, True, True, False, True, False, True, False, True, True, False]
[True, False, True, True, False, True, False, True, True, True, True, True]
[True, False, True, True, False, True, False, True, True, True, True, True]

Is a subset exist whose sum equal to 11 ? True
"""
