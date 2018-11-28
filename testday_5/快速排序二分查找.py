def QickSort(arr,firstindex,lastindex):
    if firstindex<lastindex:
        dividindex = partition(arr,firstindex,lastindex)
        QickSort(arr,firstindex,dividindex)
        QickSort(arr,dividindex+1,lastindex)
    else:
        return
def partition(arr,firstindex,lastindex):
    i = firstindex-1
    for j in range(firstindex,lastindex):
        if arr[j]<=arr[lastindex]:
            i=i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[lastindex] = arr[lastindex],arr[i+1]
    return i
def binary_search(list,num):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low+high)//2
        var = list[mid]
        if var==num:
            return ("您查找的数字在数组中，它是：%-2.0f"%num)
        if var<num:
            low = mid+1
        else:
            high = mid-1
    return ("您查找的数字%-2.0f不在此数组中"%num)
arr = [-65,63,25,54,89,65,31,25,20]
print("初始数组为",arr)
QickSort(arr,0,len(arr)-1)
print("排序后的数组为",arr)
print(binary_search(arr,33))



