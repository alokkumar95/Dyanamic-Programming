""" Equal sum partition problem
arr=[23,13,11,7,6,5,5]
Can array be partitioned into subsets such that the sum of elements in both subsets is equal

so, idea is find the sum of all elements, if sum is even i.e two subsets can be possible with equal sum
after that we will check does a subset exist with half the sum of total sum, hence this will bring down the solution to 
subsetsum problem. If subset exist with half the orininal sum and then other subset also exist with 
half the original sum then it return true else false
Leetcode 416. Partition Equal Subset Sum
Link= https://leetcode.com/problems/partition-equal-subset-sum/
"""

def subsetSum1(arr,sum1):
  t=[[-1 for _ in range(sum1+1)] for _ in range(len(arr)+1)]

  for j in range(sum1+1):
    t[0][j]=False
  for i in range(len(arr)+1):
    t[i][0]=True

  for i in range(1,len(arr)+1):
    for j in range(1,sum1+1):
      if arr[i-1]<=j:
        t[i][j]=t[i-1][j] or t[i-1][j-arr[i-1]]
      else:
        t[i][j]=t[i-1][j]

  return t[len(arr)][sum1]

def equalSumPartition(arr):
  su=0
  for item in arr:
    su+=item

  if su%2 != 0:
    return False
  elif su%2==0:
    return subsetSum1(arr,su//2)

# arr=[1,5,5,13] # o/p=False
# arr=[1,5,5,11] # o/p=True
arr=[23,13,11,7,6,5,5]
print("Does two subsets exist whose sum is equal ?",equalSumPartition(arr))
