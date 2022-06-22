arr = [1,2,3,56,78,98]
max = arr[0]
for i in range(1,len(arr)):
   if max < arr[i]:
      max = arr[i]
print(max)