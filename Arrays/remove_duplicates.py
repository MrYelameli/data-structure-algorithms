'''Input arr=[10,20,20,30,30,30]
output arr = [10,20,30]'''

#Method 1
def remove_duplicate(arr):
    temp=[]
    temp.append(arr[0])

    i=1
    while i < len(arr):
        if (arr[i-1]!=arr[i]):
            temp.append(arr[i])
        i+=1

    return temp

print(remove_duplicate([10,20,20,30,30,40,40,45,90,90]))
