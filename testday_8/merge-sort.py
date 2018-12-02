def merge(left,right):#这是合并函数
    temp = []#定义一个临时数组，用来存放合并后的数
    i,j = 0,0
    while i<len(left) and j<len(right):#分别从两组已排好序的数组中挑出较小的
        #使用append方法，将数字添加到临时数组中
        if left[i]<right[j]:
            temp.append(left[i])
            i = i+1
        else:
            temp.append(right[j])
            j = j+1
    if i >= len(left):#判断特殊情况：当left数组已经全部添加进临时数组时
        #right数组还有未添加的数，再使用extend方法将right数组剩余的数全部添加大临时数组中
            temp.extend(right[j:])
    if j >= len(right):#判断另一种特殊情况，与上一种相反
            temp.extend(left[i:])
    return temp

def merge_sort(alist):#定义切分数组的函数
    if len(alist)<=1:#当数组中只有一个元素时停止切分
        return alist#返回最后的一个元素
    else:
        mid = len(alist) // 2
        l = alist[:mid]
        r = alist[mid:]
        left = merge_sort(l)#递归调用切分数组函数，切分左边的数组
        right = merge_sort(r)#递归调用切分数组函数，切分右边的数组
        return merge(left,right)#将切分后的数组调用merge函数合并起来

alist=[69,3,2,45,67,3,2,4,45,63,24,233]
print(merge_sort(alist))

