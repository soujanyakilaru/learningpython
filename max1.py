arr = [-200,43,1,2,3,56,78,98,-1,2,10]
max = arr[0]
index = 0
for i in range(1,len(arr)):
   if max < arr[i]:
      max = arr[i]
      index = i
arr[0],arr[index] = arr[index], arr[0] 
print(arr)