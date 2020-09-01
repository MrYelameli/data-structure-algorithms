'''Counter clockwise movement'''

def counter_clockwise(arr):
    temp=arr[0]
    i=1
    while i < len(arr):
        arr[i-1]=arr[i]
        i+=1
    arr[len(arr)-1]=temp
    return arr

print(counter_clockwise([1,2,3,4,5]))