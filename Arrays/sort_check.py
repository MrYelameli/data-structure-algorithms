import sys
n = len(sys.argv[1])
a = sys.argv[1][1:n-1]

a = a.split(',')
print(a)
flag = 0
i=1
while i < len(a):
    if (float(a[i]) < float(a[i-1])):
        flag = 1
        break
    i = i+1

if (not flag):
    print("Sorted")
else:
    print("not sorted")



