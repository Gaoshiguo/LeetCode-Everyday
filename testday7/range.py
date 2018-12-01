def Insert_sort(arr):
    for i in range(1,len(arr)):
        a,b = i,i
        key = arr[i]
        while key<arr[a-1] and a-1>=0:
            a = a-1
            if a-1<0:
                a=0
        while b>a:
            arr[b] = arr[b-1]
            b = b-1
        arr[a]=key
l = [56,12,55,89,87,59]
Insert_sort(l)
print(l)
