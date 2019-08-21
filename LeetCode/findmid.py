def findMedianSortedArrays(new_sort):
	if (len(new_sort)%2)!=0:
		mid = new_sort[int(len(new_sort)/2)]
	else:
		mid = (new_sort[int(len(new_sort)/2)]+new_sort[int((len(new_sort)/2)-1)])/2
	return mid

num_1=[1,2,3,5,9,11]
print(findMedianSortedArrays(num_1))


