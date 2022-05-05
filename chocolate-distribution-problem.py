arr = [7, 3, 2, 4, 9, 12, 56]
m=3
x=[]
arr.sort()
print(arr)
for i in range(m):
    x.append(arr[i])
print(x)
max=0
for i in range(m):
    for j in range(m):
        n = arr[i]-arr[j]
        if(n>max):
            max=n
print(max)
