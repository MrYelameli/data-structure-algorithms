def max_diff(arr):
    size=len(arr)
    diff=arr[1]-arr[0]
    for i in range(1,size-1):
        temp=arr[i+1]-arr[i]
        if temp>diff:
            diff=temp
    return diff

print(max_diff([1,2,6,80,100]))