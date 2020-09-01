def reverse_array(arr,n):
    low = 0
    high = n-1
    while(low < high):
        temp = arr[low]
        arr[low] = arr[high]
        arr[high] = temp
        low+=1
        high-=1
    return arr

print(reverse_array([1,2,3,4,5],5))