#this function time complexity is O(n*n)
# def leaders_array(arr):
#     size=len(arr)
#     # flag =True
#     temp=[]
#     for i in range(0,size):
#         flag=True
#         for j in range(i+1,size):
#             if arr[i]<=arr[j]:
#                 flag=False
#                 break
#         if flag==True:
#             temp.append(arr[i])
#     return temp

def leaders_array(arr):
    size=len(arr)
    right_most=arr[size-1]
    for i in range(size-2,-1,-1):
        if right_most < arr[i]:
            print(arr[i])
            right_most=arr[i]

arr=[20,16,17,4,17,3,5,2]
leaders_array(arr)
