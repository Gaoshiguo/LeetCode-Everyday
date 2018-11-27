def QickSort(arr,firstindex,lastindex):
    if firstindex<lastindex:
        dividindex = partition(arr,firstindex,lastindex)
        QickSort(arr,firstindex,dividindex)
        QickSort(arr,dividindex+1,lastindex)
    else:
        return

def partition(arr,firstindex,lastindex):
    i=firstindex-1
    for j in range(firstindex,lastindex):
        if arr[j]<arr[lastindex]:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[lastindex] = arr[lastindex],arr[i+1]
    return i
arr = [-8,56,45,12,89,78,54,53,55]
print("初始数组为",arr)
QickSort(arr,0,len(arr)-1)
print("排序后的数组为",arr)
