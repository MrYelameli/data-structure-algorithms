'''INput arr[]= [10,10,10,25,30,30]
output : 10: 3
        25: 1
        30: 2

Input arr[]=[10,10,10,10]
    output 10:4'''

def print_freq(arr):
    n=len(arr)
    i=1
    freq=1
    while(i<n):
        while(i<n and arr[i]==arr[i-1]):
            freq+=1
            i+=1
        print(arr[i-1],":",freq)
        i+=1
        freq=1




print_freq([10,10,20])