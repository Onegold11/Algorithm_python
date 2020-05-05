def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    lList = list[:mid]
    rList = list[mid:]

    lList = merge_sort(lList)
    rList = merge_sort(rList)
    return merge(lList, rList)

def merge(lList, rList):
    result = []

    while len(lList) > 0 and len(rList) > 0:
        if lList[0] >= rList[0]:
            result.append(lList.pop(0))
        else:
            result.append(rList.pop(0))

    if len(lList) > 0:
        result += lList
    else:
        result += rList

    return result

num = input()
num_list = []

for i in range(len(num)):
    num_list.append(int(num[i]))

for num in merge_sort(num_list):
    print(num, end='')