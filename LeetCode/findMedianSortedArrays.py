def mergesort(a,b):
    ret = []
    while len(a)>0 and len(b)>0:
        if a[0] <= b[0]:
            ret.append(a[0])
            a.remove(a[0])    
        if a[0] >= b[0]:
            ret.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        ret += b
    if len(b) == 0:
        ret += a
    return ret
def findMedianSortedArrays(new_sort):
	if (len(new_sort)%2)!=0:
		mid = new_sort[int(len(new_sort)/2)]
	else:
		mid = (new_sort[int(len(new_sort)/2)]+new_sort[int((len(new_sort)/2)-1)])/2
	return mid





num_1=[1,2,3,5,9]
num_2=[2,3,7]

new_array = mergesort(num_1,num_2)
print(new_array)
print(findMedianSortedArrays(new_array))
