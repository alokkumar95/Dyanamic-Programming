""" 0-1 KnapSack Top down approach
Problem statement : Print maximum value obtain by selecting weight to to fill the sack 
"""
""" wt=weight array
    val is value array
    w weight given 
    n size of weight array
"""
import pprint
pp=pprint.PrettyPrinter()

def knapSack(wt,val,w,n):
  t=[[0] * (w+1) for _ in range(n+1)]

  for i in range(1,n+1):
    for j in range(1,w+1):

      if wt[i-1]<=j:
        t[i][j]=max(val[i-1]+t[i-1][j-wt[i-1]],t[i-1][j])
      else:
        t[i][j]=t[i-1][j]
  print("Top Down Matrix")
  pp.pprint(t)
  return t[n][w]

arr=[1,3,4,5]
val=[1,4,5,7]
w=7
print("Maximum value obtained=",knapSack(arr,val,w,len(arr)))


"""Output
Top Down Matrix
[[0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 1, 1, 1, 1, 1, 1],
 [0, 1, 1, 4, 5, 5, 5, 5],
 [0, 1, 1, 4, 5, 6, 6, 9],
 [0, 1, 1, 4, 5, 7, 8, 9]]
Maximum value obtained= 9
"""
