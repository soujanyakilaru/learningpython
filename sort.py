arr = [-200,43,1,2,3,56,78,98,-1,2,10]
for i in range(0,len(arr)):
   max = arr[i]
   index = i
   for j in range(i+1,len(arr)):
      if max < arr[j]:
         max = arr[j]
         index = j
   arr[i],arr[index] = arr[index], arr[i] 
print(arr)