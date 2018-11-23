#if else的使用
num = 3
if num<10:
    if num>5:
        print("num大小在5-10之间")
    else:
        print("num大小在0-5之间")
else:
    print("num大于10")
#写法二：
num_1 = 10
if num_1>0 and num_1<10:
    print("num大小在0-10之间")
else:
    print("num大小不在0-10之间")

#写法三：
if 5 <= num <= 10:
    print("num大小在5-10之间")
else:
    print("num大小不在5-10之间")


