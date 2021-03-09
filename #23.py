#Maximum product subarray
def maxProduct(arr, n): 
    minVal = arr[0] 
    maxVal = arr[0] 
    maxProduct = arr[0] 
    for i in range(1, n, 1): 
        if (arr[i] < 0): 
            temp = maxVal 
            maxVal = minVal 
            minVal = temp 
        maxVal = max(arr[i], maxVal * arr[i]) 
        minVal = min(arr[i], minVal * arr[i]) 
        maxProduct = max(maxProduct, maxVal) 
  
    return maxProduct
a=[2,3,4,5,-1,0]
print(maxProduct(a,len(a)))