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
        if arr[j]<=arr[lastindex]:#第四天的快速排序代码有误，当数组中有相等的数字的时候应该有等号，否则会陷入递归栈溢出的错误
            i=i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[lastindex] = arr[lastindex],arr[i+1]
    return i

#arr = [65,45,23,98,45,75,22]
arr = [65,45,23,98,45,75,22]
print("初始数组为",arr)
QickSort(arr,0,len(arr)-1)
print("排序后的数组为",arr)